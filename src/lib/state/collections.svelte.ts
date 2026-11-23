/// <reference types="svelte" />
/**
 * Collections, Favorites & Multi-Select State Store (Svelte 5 Runes)
 *
 * Preserves 100% backward compatibility with legacy `localStorage['iconstash-collections']`:
 * `Array<{ id: string, name: string, icons: string[] }>` with `"favorites"` always at index 0.
 * (See `docs/baseline-audit.md` §4.)
 */

export const COLLECTIONS_STORAGE_KEY = 'iconstash-collections';
const FAVORITES_ID = 'favorites';
const FAVORITES_NAME = 'Favorites';

export interface StoredCollectionEntry {
  id: string;
  name: string;
  icons: string[];
}

function slugifyCollectionId(name: string): string {
  const base = name
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
  return base || `collection-${Date.now()}`;
}

function isFavoritesKey(nameOrId: string): boolean {
  const lower = nameOrId.trim().toLowerCase();
  return lower === FAVORITES_ID || lower === FAVORITES_NAME.toLowerCase();
}

function dedupeIds(list: unknown): string[] {
  if (!Array.isArray(list)) return [];
  const seen = new Set<string>();
  const out: string[] = [];
  for (const item of list) {
    if (typeof item === 'string' && item.length > 0 && !seen.has(item)) {
      seen.add(item);
      out.push(item);
    }
  }
  return out;
}

function readStoredCollections(): StoredCollectionEntry[] {
  const fallback: StoredCollectionEntry[] = [
    { id: FAVORITES_ID, name: FAVORITES_NAME, icons: [] },
  ];
  if (typeof window === 'undefined') return fallback;

  try {
    const raw = window.localStorage.getItem(COLLECTIONS_STORAGE_KEY);
    if (!raw) return fallback;
    const parsed: unknown = JSON.parse(raw);
    if (!Array.isArray(parsed)) return fallback;

    let favEntry: StoredCollectionEntry | null = null;
    const others: StoredCollectionEntry[] = [];
    const seenNames = new Set<string>();

    for (const item of parsed) {
      if (!item || typeof item !== 'object') continue;
      const obj = item as Partial<StoredCollectionEntry>;
      const name = typeof obj.name === 'string' && obj.name.trim() ? obj.name.trim() : '';
      const id = typeof obj.id === 'string' && obj.id.trim() ? obj.id.trim() : '';
      const icons = dedupeIds(obj.icons);

      if (id === FAVORITES_ID || name.toLowerCase() === FAVORITES_ID) {
        if (!favEntry) {
          favEntry = { id: FAVORITES_ID, name: FAVORITES_NAME, icons };
        } else {
          favEntry.icons = dedupeIds([...favEntry.icons, ...icons]);
        }
        continue;
      }

      if (!name) continue;
      const key = name.toLowerCase();
      if (seenNames.has(key)) continue;
      seenNames.add(key);

      others.push({
        id: id || slugifyCollectionId(name),
        name,
        icons,
      });
    }

    return [
      favEntry ?? { id: FAVORITES_ID, name: FAVORITES_NAME, icons: [] },
      ...others,
    ];
  } catch {
    return fallback;
  }
}

function writeStoredCollections(entries: readonly StoredCollectionEntry[]): void {
  if (typeof window === 'undefined') return;
  try {
    window.localStorage.setItem(COLLECTIONS_STORAGE_KEY, JSON.stringify(entries));
  } catch {
    // Ignore quota/private-mode errors
  }
}

function entriesToState(entries: readonly StoredCollectionEntry[]): {
  favorites: string[];
  collections: Record<string, string[]>;
  idMap: Map<string, string>;
} {
  let favorites: string[] = [];
  const collections: Record<string, string[]> = {};
  const idMap = new Map<string, string>();

  for (const entry of entries) {
    if (entry.id === FAVORITES_ID) {
      favorites = [...entry.icons];
      collections[FAVORITES_NAME] = [...entry.icons];
      idMap.set(FAVORITES_NAME, FAVORITES_ID);
    } else {
      collections[entry.name] = [...entry.icons];
      idMap.set(entry.name, entry.id);
    }
  }

  if (!(FAVORITES_NAME in collections)) {
    collections[FAVORITES_NAME] = [];
    idMap.set(FAVORITES_NAME, FAVORITES_ID);
  }

  return { favorites, collections, idMap };
}

class CollectionsStore {
  favorites = $state<string[]>([]);
  collections = $state<Record<string, string[]>>({ [FAVORITES_NAME]: [] });
  selectedIds = $state.raw<Set<string>>(new Set());
  selectMode = $state(false);

  private collectionIds = new Map<string, string>([[FAVORITES_NAME, FAVORITES_ID]]);

  constructor() {
    const initial = readStoredCollections();
    const hydrated = entriesToState(initial);
    this.favorites = hydrated.favorites;
    this.collections = hydrated.collections;
    this.collectionIds = hydrated.idMap;
  }

  private persist(): void {
    const entries: StoredCollectionEntry[] = [
      {
        id: FAVORITES_ID,
        name: FAVORITES_NAME,
        icons: [...this.favorites],
      },
    ];

    for (const [name, icons] of Object.entries(this.collections)) {
      if (isFavoritesKey(name)) continue;
      entries.push({
        id: this.collectionIds.get(name) ?? slugifyCollectionId(name),
        name,
        icons: [...icons],
      });
    }

    writeStoredCollections(entries);
  }

  isFavorite(id: string): boolean {
    return this.favorites.includes(id);
  }

  toggleFavorite(id: string): boolean {
    if (!id) return false;
    const exists = this.favorites.includes(id);
    const next = exists
      ? this.favorites.filter((item) => item !== id)
      : [...this.favorites, id];
    this.favorites = next;
    this.collections = {
      ...this.collections,
      [FAVORITES_NAME]: [...next],
    };
    this.persist();
    return !exists;
  }

  createCollection(name: string): boolean {
    const trimmed = name.trim();
    if (!trimmed || isFavoritesKey(trimmed)) return false;
    const lower = trimmed.toLowerCase();
    for (const existing of Object.keys(this.collections)) {
      if (existing.toLowerCase() === lower) return false;
    }
    this.collectionIds.set(trimmed, slugifyCollectionId(trimmed));
    this.collections = {
      ...this.collections,
      [trimmed]: [],
    };
    this.persist();
    return true;
  }

  deleteCollection(name: string): boolean {
    const trimmed = name.trim();
    if (!trimmed || isFavoritesKey(trimmed)) return false;
    if (!(trimmed in this.collections)) return false;

    const next = { ...this.collections };
    delete next[trimmed];
    this.collectionIds.delete(trimmed);
    this.collections = next;
    this.persist();
    return true;
  }

  renameCollection(oldName: string, newName: string): boolean {
    const from = oldName.trim();
    const to = newName.trim();
    if (!from || !to || isFavoritesKey(from) || isFavoritesKey(to)) return false;
    if (!(from in this.collections)) return false;
    if (from === to) return true;

    const lowerTo = to.toLowerCase();
    for (const existing of Object.keys(this.collections)) {
      if (existing !== from && existing.toLowerCase() === lowerTo) return false;
    }

    const next: Record<string, string[]> = {};
    for (const [k, v] of Object.entries(this.collections)) {
      if (k === from) {
        next[to] = v;
      } else {
        next[k] = v;
      }
    }

    const preservedId = this.collectionIds.get(from) ?? slugifyCollectionId(to);
    this.collectionIds.delete(from);
    this.collectionIds.set(to, preservedId);
    this.collections = next;
    this.persist();
    return true;
  }

  addToCollection(name: string, id: string): void {
    if (!id) return;
    const targetName = isFavoritesKey(name) ? FAVORITES_NAME : name.trim();
    if (!targetName) return;

    const current = this.collections[targetName] ?? [];
    if (current.includes(id)) return;

    const nextList = [...current, id];
    if (targetName === FAVORITES_NAME) {
      this.favorites = nextList;
    } else if (!this.collectionIds.has(targetName)) {
      this.collectionIds.set(targetName, slugifyCollectionId(targetName));
    }

    this.collections = {
      ...this.collections,
      [targetName]: nextList,
    };
    this.persist();
  }

  removeFromCollection(name: string, id: string): void {
    const targetName = isFavoritesKey(name) ? FAVORITES_NAME : name.trim();
    if (!targetName || !(targetName in this.collections)) return;

    const current = this.collections[targetName];
    if (!current.includes(id)) return;

    const nextList = current.filter((item) => item !== id);
    if (targetName === FAVORITES_NAME) {
      this.favorites = nextList;
    }

    this.collections = {
      ...this.collections,
      [targetName]: nextList,
    };
    this.persist();
  }

  toggleSelect(id: string): void {
    if (!id) return;
    const next = new Set(this.selectedIds);
    if (next.has(id)) {
      next.delete(id);
    } else {
      next.add(id);
    }
    this.selectedIds = next;
  }

  selectAll(ids: Iterable<string>): void {
    const next = new Set(this.selectedIds);
    for (const id of ids) {
      if (id) next.add(id);
    }
    this.selectedIds = next;
  }

  clearSelection(): void {
    if (this.selectedIds.size === 0) return;
    this.selectedIds = new Set();
  }

  setSelectMode(active: boolean): void {
    this.selectMode = active;
    if (!active) {
      this.clearSelection();
    }
  }

  toggleSelectMode(): void {
    this.setSelectMode(!this.selectMode);
  }
}

export const collectionsState = new CollectionsStore();
