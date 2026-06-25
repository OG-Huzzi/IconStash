#!/usr/bin/env node
/* eslint-disable no-console */

const fs = require("node:fs");
const path = require("node:path");

const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");
const OUT_DIR = path.join(ROOT, "icons");
const SITEMAP_DIR = path.join(ROOT, "sitemaps");
const HTML_SITEMAP_DIR = path.join(ROOT, "seo");
const KEYWORD_DB = path.join(DATA_DIR, "pseo-keywords.json");
const SITE_URL = (process.env.SITE_URL || "https://iconstash.io").replace(/\/+$/, "");
const PAGE_LIMIT = Math.max(1, Number(process.env.PSEO_LIMIT || 150000));
const TODAY = new Date().toISOString().slice(0, 10);

/* ─── Category rules ─────────────────────────────────────────────────────── */
const CATEGORY_RULES = [
  ["Media", "Photography", /camera|image|photo|video|film|play|pause|music|mic|speaker|audio|volume|gallery|picture|podcast/i],
  ["Communication", "Messaging", /mail|message|chat|comment|phone|call|send|inbox|reply|share|bell|notification/i],
  ["Commerce", "Payments", /cart|shop|bag|store|cash|coin|credit|card|wallet|bank|receipt|ticket|tag|gift/i],
  ["Navigation", "Maps", /map|pin|location|compass|route|arrow|chevron|direction|sign|road|globe/i],
  ["Files", "Documents", /file|folder|document|book|note|clipboard|archive|copy|paper|pdf|code/i],
  ["Editing", "Design", /edit|pen|pencil|brush|crop|palette|color|magic|wand|scissors|ruler|layout/i],
  ["Devices", "Hardware", /phone|mobile|tablet|laptop|desktop|monitor|keyboard|mouse|printer|watch|cpu|server|database/i],
  ["Development", "Code", /code|terminal|bug|git|branch|merge|api|webhook|cloud|database|server|package/i],
  ["Security", "Privacy", /lock|unlock|shield|key|fingerprint|scan|secure|vpn|password|verified/i],
  ["Health", "Medical", /heart|pulse|medical|hospital|doctor|pill|virus|health|first|aid|stethoscope/i],
  ["Weather", "Nature", /sun|moon|cloud|rain|snow|wind|leaf|tree|flower|fire|water|earth/i],
  ["Transport", "Travel", /car|bus|train|plane|ship|bike|truck|taxi|rocket|suitcase|luggage/i],
  ["Social", "People", /user|person|people|team|group|face|smile|emoji|profile|account/i],
  ["Time", "Productivity", /clock|time|calendar|timer|alarm|hour|watch|schedule|history/i],
  ["Data", "Charts", /chart|graph|analytics|stats|database|table|trend|activity|bar|pie/i]
];

/* ─── Synonyms for keyword expansion ─────────────────────────────────────── */
const SYNONYMS = {
  calendar: ["date", "schedule", "event"],
  camera: ["photo", "image", "snapshot"],
  search: ["find", "magnifier", "lookup"],
  user: ["profile", "person", "account"],
  users: ["team", "people", "group"],
  arrow: ["direction", "navigation", "pointer"],
  home: ["house", "dashboard", "start"],
  settings: ["gear", "preferences", "controls"],
  heart: ["favorite", "like", "love"],
  star: ["rating", "favorite", "bookmark"],
  download: ["save", "export", "install"],
  upload: ["send", "import", "publish"],
  trash: ["delete", "remove", "bin"],
  lock: ["secure", "privacy", "password"],
  chart: ["analytics", "graph", "report"],
  cart: ["shopping", "checkout", "store"],
  mail: ["email", "message", "inbox"],
  phone: ["call", "mobile", "contact"],
  check: ["confirm", "tick", "done"],
  close: ["dismiss", "cancel", "exit"],
  menu: ["hamburger", "navigation", "sidebar"],
  plus: ["add", "create", "new"],
  minus: ["remove", "subtract", "reduce"],
  eye: ["view", "visibility", "preview"],
  link: ["url", "hyperlink", "connect"],
  share: ["distribute", "send", "export"],
  refresh: ["reload", "sync", "update"],
  filter: ["sort", "refine", "search"],
  grid: ["layout", "columns", "gallery"],
  list: ["items", "index", "rows"],
  info: ["information", "details", "help"],
  warning: ["alert", "caution", "notice"],
  error: ["danger", "fail", "invalid"],
  success: ["done", "complete", "valid"]
};

/* ─── Category intents for keyword generation ────────────────────────────── */
const CATEGORY_INTENTS = {
  Media: ["for websites", "for UI design", "for apps"],
  Communication: ["for messaging apps", "for contact pages", "for dashboards"],
  Commerce: ["for ecommerce", "for checkout UI", "for stores"],
  Navigation: ["for menus", "for navigation UI", "for maps"],
  Files: ["for documents", "for admin panels", "for file managers"],
  Editing: ["for design tools", "for editors", "for creative apps"],
  Devices: ["for device UI", "for dashboards", "for product pages"],
  Development: ["for developer tools", "for documentation", "for dashboards"],
  Security: ["for security UI", "for login screens", "for privacy pages"],
  Health: ["for health apps", "for dashboards", "for wellness UI"],
  Weather: ["for weather apps", "for widgets", "for dashboards"],
  Transport: ["for travel apps", "for booking UI", "for maps"],
  Social: ["for social apps", "for profiles", "for teams"],
  Time: ["for calendar apps", "for schedules", "for productivity UI"],
  Data: ["for analytics", "for reports", "for dashboards"],
  Interface: ["for product UI", "for websites", "for apps"]
};

/* ─── Category use-case descriptions (for body copy variation) ───────────── */
const CATEGORY_CONTEXT = {
  Media: "media players, streaming interfaces, audio controls, photo galleries, podcast apps, and video platforms",
  Communication: "messaging apps, email clients, contact forms, notification systems, CRM dashboards, and live chat widgets",
  Commerce: "e-commerce checkout flows, shopping carts, payment UI, product listings, storefronts, and fintech apps",
  Navigation: "app menus, breadcrumbs, map interfaces, multi-step forms, pagination controls, and sidebar navigation",
  Files: "document management systems, admin panels, file explorers, CMS dashboards, cloud storage UIs, and PDF viewers",
  Editing: "rich text editors, design tools, image editors, drawing apps, content creation platforms, and creative suites",
  Devices: "device dashboards, IoT interfaces, product settings pages, hardware control panels, and tech product sites",
  Development: "developer tools, CLI documentation, API dashboards, GitHub-integrated UIs, code editors, and DevOps panels",
  Security: "login and authentication flows, permission management panels, privacy settings, VPN apps, and security dashboards",
  Health: "health and fitness apps, medical record systems, wellness dashboards, telemedicine platforms, and patient portals",
  Weather: "weather forecast apps, climate dashboards, location-based services, environmental widgets, and IoT sensor displays",
  Transport: "travel booking platforms, fleet management dashboards, logistics apps, ride-hailing UIs, and route planners",
  Social: "social networks, community forums, profile pages, team collaboration tools, and user management dashboards",
  Time: "calendar apps, scheduling tools, time-tracking platforms, project management dashboards, and productivity suites",
  Data: "analytics dashboards, business intelligence tools, reporting platforms, data visualization apps, and KPI displays",
  Interface: "general-purpose product UIs, design systems, component libraries, web applications, and marketing sites"
};

/* ─── Icon style descriptions ────────────────────────────────────────────── */
const STYLE_DESC = {
  outline: "uses stroked lines with no fill — clean, legible, and versatile at any size",
  filled: "uses solid filled shapes — high contrast, instantly recognizable, and bold at small sizes",
  thin: "uses ultra-fine strokes for an elegant, premium look suited to large display sizes",
  light: "uses light-weight strokes that pair well with thin typography and minimalist layouts",
  sharp: "uses straight corners and rigid geometry — structured, technical, and precise",
  duotone: "uses a two-tone composition combining primary and secondary color layers for depth",
  pixel: "uses pixel-perfect square forms for retro aesthetics and game-inspired design",
  animated: "uses SVG path animations for smooth, dynamic UI transitions and feedback",
  variable: "uses variable-font technology allowing adjustable weight, fill, grade, and optical size",
  "multi-style": "is available in multiple weights and styles including outline, filled, and specialty variants"
};

const STYLE_USE_CASES = {
  outline: "app navigation bars, toolbar buttons, form labels, and UI controls where clarity at 16–24px is critical",
  filled: "primary action buttons, selected states, status indicators, and high-emphasis interface elements",
  thin: "editorial layouts, hero sections, premium marketing pages, and large-format typographic contexts",
  light: "subtle decorative accents, secondary labels, light-themed dashboards, and minimal product pages",
  sharp: "enterprise software interfaces, admin panels, technical documentation, and structured data UIs",
  duotone: "feature highlight cards, onboarding illustrations, content-rich landing pages, and infographics",
  pixel: "retro-themed interfaces, gaming UIs, pixel art projects, and creative portfolio sites",
  animated: "loading indicators, success/error toasts, onboarding walkthrough flows, and interactive demos",
  variable: "design systems requiring a single icon source that scales across light, regular, and bold contexts",
  "multi-style": "design systems that need consistent icons across filled and outline usage in the same product"
};

/* ─── Library info for authority cards and code snippets ─────────────────── */
function toPascalCase(str) {
  return String(str || "").split(/[-_\s]+/).filter(Boolean)
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1)).join("");
}

const LIBRARY_INFO = {
  lucide: {
    fullName: "Lucide Icons", count: "1,979", style: "outline", license: "MIT",
    npm: "lucide-react",
    desc: "Clean, consistent, and MIT-licensed icon library built by the open-source community as a fork of Feather Icons. Every icon sits on a 24×24 grid with a 2px default stroke.",
    reactCode: (n) => `npm install lucide-react\n\nimport { ${toPascalCase(n)} } from 'lucide-react';\n\n// JSX usage:\n<${toPascalCase(n)} size={24} color="#000" />`
  },
  tabler: {
    fullName: "Tabler Icons", count: "6,324", style: "outline", license: "MIT",
    npm: "@tabler/icons-react",
    desc: "Free and open-source icon set with 6,300+ icons on a consistent 24px grid. One of the largest MIT-licensed outline icon libraries available.",
    reactCode: (n) => `npm install @tabler/icons-react\n\nimport { Icon${toPascalCase(n)} } from '@tabler/icons-react';\n\n// JSX usage:\n<Icon${toPascalCase(n)} size={24} stroke={1.5} />`
  },
  phosphor: {
    fullName: "Phosphor Icons", count: "9,198", style: "multi-style", license: "MIT",
    npm: "phosphor-react",
    desc: "Flexible icon family with 9,000+ icons across six weights: Thin, Light, Regular, Bold, Fill, and Duotone. Designed to work together at any scale.",
    reactCode: (n) => `npm install phosphor-react\n\nimport { ${toPascalCase(n)} } from 'phosphor-react';\n\n// JSX usage:\n<${toPascalCase(n)} size={24} weight="regular" />`
  },
  material: {
    fullName: "Material Design Icons", count: "14,001", style: "multi-style", license: "Apache 2.0",
    npm: "@mui/icons-material",
    desc: "Google's official icon set for Material Design. 14,000+ icons in five themes: Outlined, Rounded, Sharp, Two Tone, and Filled. Used across Android and web Google products.",
    reactCode: (n) => `npm install @mui/icons-material\n\nimport ${toPascalCase(n)}Outlined from '@mui/icons-material/${toPascalCase(n)}Outlined';\n\n// JSX usage:\n<${toPascalCase(n)}Outlined fontSize="small" />`
  },
  remix: {
    fullName: "Remix Icon", count: "3,244", style: "two-style", license: "Apache 2.0",
    npm: "remixicon",
    desc: "Open-source, neutral-style system icon set for designers and developers. 3,200+ icons in both line and fill variants, organized across 25 categories.",
    reactCode: (n) => `npm install remixicon\n\n/* In your CSS: */\n@import 'remixicon/fonts/remixicon.css';\n\n<!-- HTML usage: -->\n<i class="ri-${n}-line ri-lg"></i>`
  },
  iconoir: {
    fullName: "Iconoir", count: "2,020", style: "outline", license: "MIT",
    npm: "iconoir-react",
    desc: "High-quality, free SVG outline icons for UI design. 2,000+ consistent 24×24 icons with no premium tier — open and available for any project.",
    reactCode: (n) => `npm install iconoir-react\n\nimport { ${toPascalCase(n)} } from 'iconoir-react';\n\n// JSX usage:\n<${toPascalCase(n)} width={24} height={24} />`
  },
  heroicons: {
    fullName: "Heroicons", count: "1,297", style: "outline/solid", license: "MIT",
    npm: "@heroicons/react",
    desc: "Hand-crafted SVG icons by the makers of Tailwind CSS. Available in outline and solid variants at 16px, 20px, and 24px — perfect for Tailwind-based projects.",
    reactCode: (n) => `npm install @heroicons/react\n\nimport { ${toPascalCase(n)}Icon } from '@heroicons/react/24/outline';\n\n// JSX usage:\n<${toPascalCase(n)}Icon className="h-6 w-6 text-gray-700" />`
  },
  bootstrap: {
    fullName: "Bootstrap Icons", count: "2,090", style: "multi-style", license: "MIT",
    npm: "bootstrap-icons",
    desc: "Official open-source SVG icon library for Bootstrap. 2,000+ icons spanning fills, strokes, and mixed styles — built by the Bootstrap team.",
    reactCode: (n) => `npm install react-icons\n\nimport { Bi${toPascalCase(n)} } from 'react-icons/bi';\n\n// JSX usage:\n<Bi${toPascalCase(n)} size={24} />`
  },
  feather: {
    fullName: "Feather Icons", count: "286", style: "outline", license: "MIT",
    npm: "react-feather",
    desc: "Simply beautiful, minimal open-source icons. 286 carefully crafted outline icons on a 24px grid. One of the most-forked icon libraries on GitHub.",
    reactCode: (n) => `npm install react-feather\n\nimport { ${toPascalCase(n)} } from 'react-feather';\n\n// JSX usage:\n<${toPascalCase(n)} size={24} color="#000" />`
  },
  mingcute: {
    fullName: "MingCute Icons", count: "3,352", style: "multi-style", license: "Apache 2.0",
    npm: "@mingcute/icon-react",
    desc: "3,300+ high-quality icons with both line and filled variants. Clean, modern aesthetic designed for polished product interfaces and design systems.",
    reactCode: (n) => `npm install @mingcute/icon-react\n\nimport { ${toPascalCase(n)}Line } from '@mingcute/icon-react';\n\n// JSX usage:\n<${toPascalCase(n)}Line size={24} />`
  },
  solar: {
    fullName: "Solar Icons", count: "7,410", style: "multi-style", license: "CC BY 4.0",
    npm: "solar-icon-set",
    desc: "Premium icon pack with 7,400+ icons across six styles: Linear, Outline, Bold, Duotone, Broken, and Bold Duotone. Widely used in SaaS and mobile product design.",
    reactCode: (n) => `npm install solar-icon-set\n\nimport ${toPascalCase(n)} from 'solar-icon-set/${toPascalCase(n)}';\n\n// JSX usage:\n<${toPascalCase(n)} size={24} iconStyle="Linear" />`
  },
  octicons: {
    fullName: "Octicons", count: "929", style: "outline", license: "MIT",
    npm: "@primer/octicons-react",
    desc: "GitHub's design-system icon library. 900+ interface icons used across GitHub.com, GitHub Desktop, GitHub Mobile, and GitHub Docs.",
    reactCode: (n) => `npm install @primer/octicons-react\n\nimport { ${toPascalCase(n)}Icon } from '@primer/octicons-react';\n\n// JSX usage:\n<${toPascalCase(n)}Icon size={24} />`
  },
  cssgg: {
    fullName: "css.gg Icons", count: "705", style: "outline", license: "MIT",
    npm: "css.gg",
    desc: "700+ open-source icons available as pure CSS, SVG, and npm packages. Each icon is a single CSS file with no external dependencies.",
    reactCode: (n) => `npm install css.gg\n\n/* Import the specific icon CSS */\n@import url('css.gg/icons/css/${n}.css');\n\n<!-- HTML usage: -->\n<i class="gg-${n}"></i>`
  },
  radix: {
    fullName: "Radix Icons", count: "345", style: "outline", license: "MIT",
    npm: "@radix-ui/react-icons",
    desc: "Crisp 15×15 icons from the Radix UI team — designed for precise placement in dense product interfaces alongside Radix Primitives.",
    reactCode: (n) => `npm install @radix-ui/react-icons\n\nimport { ${toPascalCase(n)}Icon } from '@radix-ui/react-icons';\n\n// JSX usage:\n<${toPascalCase(n)}Icon width={24} height={24} />`
  },
  antdesign: {
    fullName: "Ant Design Icons", count: "1,870", style: "multi-style", license: "MIT",
    npm: "@ant-design/icons",
    desc: "Official icon library for Ant Design — China's leading enterprise React UI framework. 1,800+ icons in Outlined, Filled, and TwoTone styles.",
    reactCode: (n) => `npm install @ant-design/icons\n\nimport { ${toPascalCase(n)}Outlined } from '@ant-design/icons';\n\n// JSX usage:\n<${toPascalCase(n)}Outlined style={{ fontSize: '24px' }} />`
  },
  fluent: {
    fullName: "Fluent UI Icons", count: "20,170", style: "multi-style", license: "MIT",
    npm: "@fluentui/react-icons",
    desc: "Microsoft's Fluent Design System icon library with 20,000+ icons across multiple sizes (12–48px) and styles (Regular, Filled). Used across Microsoft 365 products.",
    reactCode: (n) => `npm install @fluentui/react-icons\n\nimport { ${toPascalCase(n)}Regular } from '@fluentui/react-icons';\n\n// JSX usage:\n<${toPascalCase(n)}Regular fontSize={24} />`
  },
  carbon: {
    fullName: "Carbon Icons", count: "2,644", style: "outline", license: "Apache 2.0",
    npm: "@carbon/icons-react",
    desc: "IBM's open-source icon library aligned with the Carbon Design System. 2,600+ enterprise-grade icons maintained by IBM's design team.",
    reactCode: (n) => `npm install @carbon/icons-react\n\nimport { ${toPascalCase(n)} } from '@carbon/icons-react';\n\n// JSX usage:\n<${toPascalCase(n)} size={24} />`
  },
  ionicons: {
    fullName: "Ionicons", count: "2,607", style: "multi-style", license: "MIT",
    npm: "ionicons",
    desc: "Beautifully crafted open-source icons built for Ionic Framework. 2,600+ icons in Outline, Filled, and Sharp variants — works in any web framework.",
    reactCode: (n) => `npm install @ionic/react ionicons\n\nimport { IonIcon } from '@ionic/react';\nimport { ${n.replace(/-/g, "")} } from 'ionicons/icons';\n\n// JSX usage:\n<IonIcon icon={${n.replace(/-/g, "")}} style={{ fontSize: '24px' }} />`
  },
  eva: {
    fullName: "Eva Icons", count: "490", style: "outline/filled", license: "MIT",
    npm: "eva-icons",
    desc: "480+ beautifully crafted open-source SVG icons for common UI actions and items. Available in Fill and Outline styles with consistent 24px sizing.",
    reactCode: (n) => `npm install react-eva-icons\n\nimport EvaIcon from 'react-eva-icons';\n\n// JSX usage:\n<EvaIcon name="${n}" size="24" fill="#000" />`
  },
  boxicons: {
    fullName: "Boxicons", count: "3,389", style: "multi-style", license: "MIT",
    npm: "boxicons",
    desc: "High-quality web icons by Atisa. 3,300+ carefully crafted icons in Regular, Solid, and Logos variants. One of the most popular free icon packs for web development.",
    reactCode: (n) => `npm install react-icons\n\nimport { Bx${toPascalCase(n)} } from 'react-icons/bx';\n\n// JSX usage:\n<Bx${toPascalCase(n)} size={24} />`
  },
  materialsymbols: {
    fullName: "Material Symbols", count: "18,547", style: "variable", license: "Apache 2.0",
    npm: "@material-symbols/svg-400",
    desc: "Google's newest icon format built on variable font technology. 18,500+ icons with four adjustable axes: Weight, Fill, Grade, and Optical Size — all from a single file.",
    reactCode: (n) => `/* Use Google Fonts CDN */\n<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet">\n\n<!-- HTML usage: -->\n<span class="material-symbols-outlined">${n.replace(/-/g, "_")}</span>`
  },
  materialsymbolslight: {
    fullName: "Material Symbols Light", count: "15,969", style: "light", license: "Apache 2.0",
    npm: "@material-symbols/svg-300",
    desc: "The 300-weight light variant of Google's Material Symbols. 15,900+ icons optimized for elegant, subtle interfaces where a lighter visual weight is preferred.",
    reactCode: (n) => `/* Use Google Fonts CDN (weight=300) */\n<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@300" rel="stylesheet">\n\n<!-- HTML usage: -->\n<span class="material-symbols-outlined">${n.replace(/-/g, "_")}</span>`
  },
  iconparkoutline: {
    fullName: "IconPark Outline", count: "2,658", style: "outline", license: "Apache 2.0",
    npm: "@icon-park/react",
    desc: "ByteDance's outline icon library with 2,600+ colorful, highly customizable icons for web and mobile apps. Supports dynamic color configuration.",
    reactCode: (n) => `npm install @icon-park/react\n\nimport { ${toPascalCase(n)} } from '@icon-park/react';\n\n// JSX usage:\n<${toPascalCase(n)} theme="outline" size={24} fill="#000" />`
  },
  iconparksolid: {
    fullName: "IconPark Solid", count: "1,970", style: "filled", license: "Apache 2.0",
    npm: "@icon-park/react",
    desc: "ByteDance's filled/solid icon library with 1,900+ solid-style icons. Fully customizable colors and sizes, built on the same system as IconPark Outline.",
    reactCode: (n) => `npm install @icon-park/react\n\nimport { ${toPascalCase(n)} } from '@icon-park/react';\n\n// JSX usage:\n<${toPascalCase(n)} theme="filled" size={24} fill="#000" />`
  },
  hugeicons: {
    fullName: "Huge Icons", count: "5,115", style: "multi-style", license: "MIT",
    npm: "hugeicons-react",
    desc: "5,100+ premium-quality SVG icons in 6 styles: Stroke, Duotone, Solid, Bulk, Twotone, and Sharp Stroke. Designed by HugeIcons for professional product interfaces.",
    reactCode: (n) => `npm install hugeicons-react\n\nimport { ${toPascalCase(n)}Icon } from 'hugeicons-react';\n\n// JSX usage:\n<${toPascalCase(n)}Icon size={24} color="#000" />`
  },
  pixelarticons: {
    fullName: "Pixel Art Icons", count: "1,099", style: "pixel", license: "MIT",
    npm: "pixelarticons",
    desc: "1,000+ pixel art style SVG icons for retro aesthetics, game-inspired interfaces, and creative projects. Designed on a strict pixel grid.",
    reactCode: (n) => `npm install pixelarticons\n\n<!-- Direct SVG import (recommended) -->\n<img src="node_modules/pixelarticons/svg/${n}.svg" alt="${n}" width="24" height="24">`
  },
  linemd: {
    fullName: "Line MD Icons", count: "1,279", style: "animated", license: "MIT",
    npm: "@iconify/react",
    desc: "1,200+ animated SVG line icons with smooth path animations. Perfect for loading states, success feedback, onboarding flows, and interactive interfaces.",
    reactCode: (n) => `npm install @iconify/react\n\nimport { Icon } from '@iconify/react';\n\n// JSX usage (via Iconify):\n<Icon icon="line-md:${n}" width={24} height={24} />`
  },
  simpleicons: {
    fullName: "Simple Icons", count: "3,714", style: "filled", license: "CC0 1.0",
    npm: "simple-icons",
    desc: "3,700+ free SVG brand icons for popular technologies, platforms, companies, and products. The definitive source for brand logos in tech stacks and README files.",
    reactCode: (n) => `npm install simple-icons react-icons\n\nimport { Si${toPascalCase(n)} } from 'react-icons/si';\n\n// JSX usage:\n<Si${toPascalCase(n)} size={24} />`
  }
};

/* ─── Deterministic hash (for content variation without randomness) ───────── */
function hashCode(str) {
  let h = 5381;
  for (let i = 0; i < str.length; i++) h = ((h << 5) + h) ^ str.charCodeAt(i);
  return Math.abs(h >>> 0);
}

/* ─── Core utility functions (unchanged) ─────────────────────────────────── */
function readJson(file) {
  return JSON.parse(fs.readFileSync(file, "utf8"));
}
function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}
function cleanOutput() {
  fs.rmSync(OUT_DIR, { recursive: true, force: true });
  fs.rmSync(SITEMAP_DIR, { recursive: true, force: true });
  fs.rmSync(HTML_SITEMAP_DIR, { recursive: true, force: true });
  ensureDir(OUT_DIR);
  ensureDir(SITEMAP_DIR);
  ensureDir(HTML_SITEMAP_DIR);
}
function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
function slugify(value) {
  return String(value || "")
    .toLowerCase()
    .replace(/&/g, " and ")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}
function titleCase(value) {
  return String(value || "")
    .split(/[-_\s]+/)
    .filter(Boolean)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}
function displayName(raw) {
  return titleCase(String(raw || "icon")
    .replace(/^(baseline|outline|round|sharp|twotone)-/, "")
    .replace(/_(24|20|16|12)$/, "")
    .replace(/-/g, " "));
}
function baseName(name) {
  return slugify(String(name || "")
    .replace(/\b(outline|regular|solid|filled|fill|bold|duotone|thin|light|sharp|round|linear|twotone|two tone|24|20|16|12)\b/gi, ""));
}
function deriveStyle(name, prefix) {
  const text = `${prefix || ""}-${name || ""}`.toLowerCase();
  if (/duotone|two-tone|twotone/.test(text)) return "duotone";
  if (/bold|filled|fill|solid|bxs-/.test(text)) return "filled";
  if (/thin/.test(text)) return "thin";
  if (/light/.test(text)) return "light";
  if (/sharp/.test(text)) return "sharp";
  if (/regular|outline|linear|stroke|lucide|tabler|feather|iconoir|radix|hugeicons|line-md/.test(text)) return "outline";
  return "filled";
}
function categorize(name) {
  const match = CATEGORY_RULES.find(([, , rx]) => rx.test(name));
  return match ? [match[0], match[1]] : ["Interface", "Controls"];
}
function normalizeBody(body) {
  const content = String(body || "");
  if (!/<(path|g|circle|rect|line|polyline|polygon|ellipse|defs|use|clipPath|mask)\b/i.test(content)) {
    return `<path d="${escapeHtml(content)}"></path>`;
  }
  return content
    .replace(/\s(fill|stroke)="(?!none\b|transparent\b|url\(|freeze\b|remove\b)[^"]*"/gi, (_m, a) => ` ${a}="currentColor"`)
    .replace(/\s(fill|stroke)='(?!none\b|transparent\b|url\(|freeze\b|remove\b)[^']*'/gi, (_m, a) => ` ${a}="currentColor"`);
}
function renderSvg(icon, size = 72) {
  const fill = icon.style === "filled" ? "currentColor" : "none";
  const stroke = fill === "none" ? "currentColor" : "none";
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${escapeHtml(icon.viewBox)}" width="${size}" height="${size}" fill="${fill}" stroke="${stroke}" stroke-width="${icon.strokeWidth || 2}" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="${escapeHtml(icon.name)} icon">${normalizeBody(icon.body)}</svg>`;
}

/* ─── Library normalization (unchanged) ──────────────────────────────────── */
function normalizeLibrary(lib) {
  const file = path.join(DATA_DIR, `${lib.slug}.json`);
  const data = readJson(file);
  if (Array.isArray(data)) {
    return data.map((icon, index) => {
      const name = icon.name || icon.id || "icon";
      const [category, subCategory] = icon.category ? [icon.category, icon.subCategory || "Controls"] : categorize(name);
      return {
        id: icon.id || `${lib.slug}-${slugify(name)}`,
        name, displayName: displayName(name), base: baseName(name),
        body: icon.svgPath || icon.svgContent || "",
        viewBox: icon.viewBox || `0 0 ${icon.width || 24} ${icon.height || 24}`,
        width: icon.width || 24, height: icon.height || 24,
        style: icon.style || deriveStyle(name, lib.remotePrefix || lib.slug),
        strokeWidth: icon.strokeWidth || 2, category, subCategory,
        library: lib.name, librarySlug: lib.slug,
        docsUrl: icon.docsUrl || lib.docsUrl || "",
        npmPackage: icon.npmPackage || lib.npmPackage || lib.slug,
        popularity: icon.popularity || Math.max(100, 10000 - ((index * 17) % 9900))
      };
    }).filter((icon) => icon.body);
  }
  const defaults = { width: data.width || 24, height: data.height || 24, left: data.left || 0, top: data.top || 0 };
  const prefix = data.prefix || lib.remotePrefix || lib.slug;
  const entries = Object.entries(data.icons || {}).map(([name, raw]) => [name, { ...defaults, ...raw }]);
  for (const [name, alias] of Object.entries(data.aliases || {})) {
    const parent = data.icons?.[alias.parent];
    if (parent?.body) entries.push([name, { ...defaults, ...parent, ...alias, body: parent.body }]);
  }
  return entries.filter(([, raw]) => raw.body).map(([rawName, raw], index) => {
    const name = rawName.replace(/^(baseline|outline|round|sharp|twotone)-/, "").replace(/_(24|20|16|12)$/, "");
    const [category, subCategory] = categorize(name);
    return {
      id: `${lib.slug}-${rawName}`.replace(/[^a-zA-Z0-9_-]/g, "-").toLowerCase(),
      name, displayName: displayName(name), base: baseName(name), body: raw.body,
      viewBox: `${raw.left || 0} ${raw.top || 0} ${raw.width || defaults.width} ${raw.height || defaults.height}`,
      width: raw.width || defaults.width, height: raw.height || defaults.height,
      style: deriveStyle(rawName, prefix),
      strokeWidth: deriveStyle(rawName, prefix) === "thin" ? 1 : 2,
      category, subCategory, library: lib.name, librarySlug: lib.slug,
      docsUrl: lib.docsUrl || "", npmPackage: lib.npmPackage || lib.slug,
      popularity: Math.max(100, 10000 - ((index * 17) % 9900))
    };
  });
}

/* ─── Keyword building (unchanged) ───────────────────────────────────────── */
function iconWords(icon) {
  const words = icon.base.split("-").filter(Boolean);
  const expanded = new Set(words);
  for (const word of words) {
    for (const synonym of SYNONYMS[word] || []) expanded.add(synonym);
  }
  return Array.from(expanded);
}
function keywordTemplates(icon) {
  const lib = icon.library.replace(/\s+Icons$/i, "");
  const name = icon.displayName.toLowerCase();
  const words = iconWords(icon).slice(0, 5);
  const primary = words[0] || "interface";
  const intents = CATEGORY_INTENTS[icon.category] || CATEGORY_INTENTS.Interface;
  return [
    { keyword: `${lib.toLowerCase()} ${name} icon svg`, format: "svg", intent: "download" },
    { keyword: `${lib.toLowerCase()} ${name} icon png`, format: "png", intent: "download" },
    { keyword: `${name} icon png`, format: "png", intent: "download" },
    { keyword: `download ${name} svg icon`, format: "svg", intent: "download" },
    { keyword: `download ${name} png icon`, format: "png", intent: "download" },
    { keyword: `${name} svg and png download`, format: "svg/png", intent: "download" },
    { keyword: `${name} ${icon.style} icon`, format: icon.style, intent: "style" },
    { keyword: `${name} icon for react`, format: "react", intent: "use" },
    { keyword: `${name} icon figma`, format: "figma", intent: "design" },
    { keyword: `copy ${name} svg`, format: "svg", intent: "copy" },
    { keyword: `${primary} icon ${intents[0]}`, format: "svg", intent: "use" },
    { keyword: `${lib.toLowerCase()} ${name} ${icon.style} svg`, format: "svg", intent: "library" }
  ];
}
function buildKeywords(icons) {
  const seen = new Set();
  const primaryRows = [];
  const secondaryRows = [];
  const candidatesByIcon = new Map();
  for (const icon of icons) {
    const templates = keywordTemplates(icon);
    const candidates = [];
    for (const item of templates) {
      const keyword = item.keyword.toLowerCase().replace(/\s+/g, " ").trim();
      const slug = slugify(keyword);
      if (!slug) continue;
      const exactNameBoost = keyword.includes(icon.base.replace(/-/g, " ")) ? 8 : 0;
      const score = Math.round((icon.popularity || 100) + exactNameBoost + (item.intent === "download" ? 60 : 0) + (item.format === "svg" ? 40 : 0));
      candidates.push({ ...item, keyword, slug, iconId: icon.id, category: icon.category, librarySlug: icon.librarySlug, score });
    }
    candidates.sort((a, b) => b.score - a.score || a.slug.localeCompare(b.slug));
    if (candidates.length > 0) candidatesByIcon.set(icon.id, candidates);
  }
  for (const candidates of candidatesByIcon.values()) {
    const best = candidates[0];
    if (!seen.has(best.slug)) { seen.add(best.slug); primaryRows.push(best); }
  }
  for (const candidates of candidatesByIcon.values()) {
    for (let i = 1; i < candidates.length; i++) {
      const cand = candidates[i];
      if (!seen.has(cand.slug)) secondaryRows.push(cand);
    }
  }
  secondaryRows.sort((a, b) => b.score - a.score || a.slug.localeCompare(b.slug));
  const rows = [...primaryRows];
  const remainingBudget = PAGE_LIMIT - rows.length;
  if (remainingBudget > 0) {
    for (const item of secondaryRows.slice(0, remainingBudget)) { seen.add(item.slug); rows.push(item); }
  }
  return rows
    .sort((a, b) => b.score - a.score || a.slug.localeCompare(b.slug))
    .map((row, index) => ({ ...row, priority: index + 1, url: `/icons/${row.slug}/` }));
}

/* ─── SEO title & meta description ───────────────────────────────────────── */
function seoTitle(keyword) {
  const base = titleCase(keyword);
  const suffix = " | SVG & PNG - IconStash";
  if ((base + suffix).length <= 60) return base + suffix;
  const download = `${base} SVG & PNG Download`;
  if (download.length <= 60) return download;
  return `${base.slice(0, 36).replace(/\s+\S*$/, "")} SVG & PNG - IconStash`;
}

function metaDescription(row, icon) {
  const name = icon.displayName;
  const lib = icon.library;
  const style = icon.style;
  const h = hashCode(icon.id) % 4;
  const templates = [
    `Download the ${name} ${style} icon from ${lib} in SVG and PNG formats. Customize color, size (16–512px), and stroke width on IconStash — free, no login required.`,
    `Copy the ${name} icon SVG code or export a custom PNG instantly. ${lib}'s ${style}-style ${name} icon is available on IconStash with React, HTML, and CSS export options.`,
    `Free ${name} icon from ${lib} — ${style} style. Download SVG or PNG, generate JSX components, and preview on any background at iconstash.io. No account needed.`,
    `Get the ${lib} ${name} icon in SVG and PNG. Set exact pixel size, pick any color, adjust stroke, and download. Available in the IconStash browser-based icon editor.`
  ];
  const text = templates[h];
  return text.length > 160 ? `${text.slice(0, 157).replace(/\s+\S*$/, "")}...` : text;
}

/* ─── AEO: 7-question FAQ per icon ───────────────────────────────────────── */
function buildFaq(row, icon, libInfo) {
  const name = icon.displayName;
  const lib = icon.library;
  const style = icon.style;
  const cat = icon.category;
  const npm = libInfo ? libInfo.npm : (icon.npmPackage || slugify(lib));
  const catCtx = CATEGORY_CONTEXT[cat] || "product interfaces and web applications";
  const styleD = STYLE_DESC[style] || "uses a clean SVG vector format";
  const styleU = STYLE_USE_CASES[style] || "interface components";
  const libD = libInfo ? libInfo.desc : `${lib} is a professionally designed open-source icon library used in modern UI development.`;
  const libCount = libInfo ? libInfo.count : "thousands of";
  const license = libInfo ? `${lib} is licensed under ${libInfo.license}, making it free for personal and commercial use.` : `${lib} is open-source. Check the library's documentation for full license terms.`;

  return [
    {
      q: `What is the ${name} icon?`,
      a: `The ${name} icon is a ${style}-style SVG icon from the ${lib} library, categorized under ${cat}. It is designed for use in ${catCtx}. On IconStash you can preview it, customize its color and size, and export it in SVG, PNG, JSX, or CSS formats directly from your browser.`
    },
    {
      q: `Is the ${name} icon free to use?`,
      a: `Yes. ${license} This means you can freely use the ${name} icon in personal, commercial, and open-source projects. IconStash provides SVG and PNG access at no cost with no login required.`
    },
    {
      q: `How do I use the ${name} icon in React?`,
      a: `Install the package with \`npm install ${npm}\`, then import the component into your React file. IconStash's detail panel shows you the exact npm command, import statement, and JSX usage snippet for every icon — just click the Code tab and copy with one click.`
    },
    {
      q: `What is the ${lib} icon library?`,
      a: `${libD} It contains ${libCount}+ icons. IconStash indexes the complete ${lib} collection alongside 27 other open-source libraries — 134,701 icons total — in a single unified search interface.`
    },
    {
      q: `Can I download the ${name} icon as a PNG?`,
      a: `Yes. Open the ${name} icon in IconStash, set your desired pixel size (16px to 512px) in the detail panel, and click Download PNG. You can also export a multi-resolution ZIP pack containing 16, 24, 32, 48, 64, 128, 256, and 512px PNGs with a single click.`
    },
    {
      q: `What does the ${style} icon style mean?`,
      a: `An icon in ${style} style ${styleD}. This style is best suited for ${styleU}. The ${lib} ${name} icon follows this visual convention throughout the ${lib} design system.`
    },
    {
      q: `Can I change the ${name} icon's color and size before downloading?`,
      a: `Yes. In IconStash's editor panel, choose from six color presets (blue, slate, green, purple, red, teal) or enter a custom hex value. Drag the size slider (16–256px) or type an exact pixel value up to 512px. Changes apply instantly to the SVG preview, the PNG output, and the copied code.`
    }
  ];
}

/* ─── GEO: HowTo + SoftwareApplication schema ────────────────────────────── */
function buildSchema(row, icon, faq, url, appUrl) {
  return [
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      itemListElement: [
        { "@type": "ListItem", position: 1, name: "IconStash", item: `${SITE_URL}/` },
        { "@type": "ListItem", position: 2, name: icon.library, item: `${SITE_URL}/#/library/${icon.librarySlug}` },
        { "@type": "ListItem", position: 3, name: icon.displayName, item: url }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      mainEntity: faq.map((item) => ({
        "@type": "Question",
        name: item.q,
        acceptedAnswer: { "@type": "Answer", text: item.a }
      }))
    },
    {
      "@context": "https://schema.org",
      "@type": "HowTo",
      name: `How to download and use the ${icon.displayName} icon`,
      description: `Step-by-step guide to finding, customizing, and exporting the ${icon.displayName} icon from ${icon.library} on IconStash.`,
      totalTime: "PT1M",
      step: [
        {
          "@type": "HowToStep", position: 1,
          name: "Open the icon in IconStash",
          text: `Go to iconstash.io and search for "${icon.name.replace(/-/g, " ")}". Click the icon card to open the detail panel, or follow the direct link to this icon's page.`,
          url: appUrl
        },
        {
          "@type": "HowToStep", position: 2,
          name: "Customize color, size, and stroke",
          text: "Select a color from the presets or type a custom hex value. Set the exact pixel size from 16px to 512px. Adjust stroke width for outline icons. Preview on dark, light, or checkered backgrounds.",
          url: appUrl
        },
        {
          "@type": "HowToStep", position: 3,
          name: "Copy SVG code or download PNG",
          text: "Use the Code tab to copy SVG markup, JSX component code, HTML img tag, or CSS background-mask. Use the Download tab to export a custom-size PNG or a multi-resolution ZIP pack.",
          url: appUrl
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      name: "IconStash",
      applicationCategory: "DesignApplication",
      operatingSystem: "Web",
      url: SITE_URL,
      description: "Browser-based icon search engine unifying 28+ open-source icon libraries into a single lightning-fast search. Search, preview, customize, and download 134,701+ SVG and PNG icons with no login required.",
      featureList: ["SVG copy", "Custom PNG download", "Multi-resolution ZIP export", "React JSX export", "CSS background-mask export", "Cross-library comparison", "Color customization", "Stroke width control", "134,701 icons from 28 libraries"],
      offers: { "@type": "Offer", price: "0", priceCurrency: "USD" },
      author: { "@type": "Organization", name: "Great Software Company", url: "https://greatsoftwarecompany.com" }
    },
    {
      "@context": "https://schema.org",
      "@type": "ImageObject",
      name: `${icon.displayName} icon`,
      description: `${icon.style} style SVG icon from ${icon.library}`,
      creator: { "@type": "Organization", name: icon.library },
      encodingFormat: "image/svg+xml",
      contentUrl: appUrl,
      license: "https://opensource.org/licenses/MIT"
    }
  ];
}

/* ─── Related links and indexes ──────────────────────────────────────────── */
const keywordsByIcon = new Map();
const keywordsByCategory = new Map();
const keywordsByLibrary = new Map();
const keywordsByFirstWord = new Map();

function buildIndexes(keywords, byIcon) {
  for (const row of keywords) {
    if (!keywordsByIcon.has(row.iconId)) keywordsByIcon.set(row.iconId, []);
    keywordsByIcon.get(row.iconId).push(row);
    if (!keywordsByCategory.has(row.category)) keywordsByCategory.set(row.category, []);
    keywordsByCategory.get(row.category).push(row);
    if (!keywordsByLibrary.has(row.librarySlug)) keywordsByLibrary.set(row.librarySlug, []);
    keywordsByLibrary.get(row.librarySlug).push(row);
    const icon = byIcon.get(row.iconId);
    if (icon) {
      const fw = icon.base.split("-")[0];
      if (fw) {
        if (!keywordsByFirstWord.has(fw)) keywordsByFirstWord.set(fw, []);
        keywordsByFirstWord.get(fw).push(row);
      }
    }
  }
}

function relatedFor(row, byIcon) {
  const icon = byIcon.get(row.iconId);
  const related = [];
  const seen = new Set([row.slug]);
  function add(list) {
    for (const item of list) {
      if (!seen.has(item.slug)) { seen.add(item.slug); related.push(item); if (related.length >= 10) return true; }
    }
    return false;
  }
  if (add(keywordsByIcon.get(row.iconId) || [])) return related;
  if (add(keywordsByCategory.get(row.category) || [])) return related;
  if (add(keywordsByLibrary.get(row.librarySlug) || [])) return related;
  if (icon) {
    const fw = icon.base.split("-")[0];
    if (fw) add(keywordsByFirstWord.get(fw) || []);
  }
  return related;
}

/* ─── Page HTML: rich, varied, GEO/AEO-ready ────────────────────────────── */
function pageHtml(row, icon, related) {
  const title = seoTitle(row.keyword);
  const description = metaDescription(row, icon);
  const url = `${SITE_URL}${row.url}`;
  const appUrl = `${SITE_URL}/#/icon/${encodeURIComponent(icon.id)}`;
  const libUrl = `${SITE_URL}/#/library/${encodeURIComponent(icon.librarySlug)}`;
  const libInfo = LIBRARY_INFO[icon.librarySlug] || null;

  const faq = buildFaq(row, icon, libInfo);
  const schema = buildSchema(row, icon, faq, url, appUrl);

  /* Deterministic variation index (0-5) per icon — never random */
  const hx = hashCode(icon.id);

  /* Lead paragraph — 6 variations */
  const catCtx = CATEGORY_CONTEXT[icon.category] || "product interfaces and web applications";
  const styleD = STYLE_DESC[icon.style] || "a clean SVG vector format";
  const libCount = libInfo ? libInfo.count : "thousands of";
  const libNpm = libInfo ? libInfo.npm : (icon.npmPackage || slugify(icon.library));
  const leadVariants = [
    `The ${icon.displayName} icon from ${icon.library} is a ${icon.style}-style SVG available in IconStash alongside ${libCount}+ other icons from the same library. Copy its SVG code, export a custom PNG, or download a React component — no account required.`,
    `Find the ${icon.library} ${icon.displayName} icon and download it in SVG or PNG format. This ${icon.style}-style icon is optimized for ${catCtx}. Customize color, size, and stroke width inside the IconStash browser editor before exporting.`,
    `IconStash indexes the ${icon.displayName} icon from ${icon.library} alongside 134,701 icons from 28 open-source libraries. It ${styleD}, making it well suited for ${catCtx}. Set an exact pixel size from 16px to 512px and download a lossless PNG in one click.`,
    `Use the ${icon.displayName} SVG icon from ${icon.library} in your ${icon.category.toLowerCase()} interface. IconStash gives you instant access to the SVG code, React JSX snippet, CSS background-mask, and custom PNG download — all from the browser with no login.`,
    `The ${icon.library} ${icon.displayName} icon uses ${styleD}. Compare it against similar icons in 27 other libraries on IconStash, adjust stroke width, change colors with a hex picker, and export at any size.`,
    `The ${icon.displayName} icon is part of the ${icon.library} collection — ${libCount}+ professional icons for ${catCtx}. On IconStash, you can preview, customize, compare across libraries, and download in SVG, PNG, JSX, or CSS format.`
  ];
  const lead = leadVariants[hx % leadVariants.length];

  /* "Use this icon" card body — 4 variations */
  const styleU = STYLE_USE_CASES[icon.style] || "interface components and product UI";
  const useVariants = [
    `<p>The ${escapeHtml(icon.displayName)} icon from ${escapeHtml(icon.library)} fits naturally in <strong>${escapeHtml(catCtx)}</strong>. Its ${escapeHtml(icon.style)} style makes it ideal for ${escapeHtml(styleU)}.</p><p class="muted">Open it in IconStash to set stroke color via presets or a custom hex value, choose an exact pixel size (16–512px), control stroke width (0.1–3px), and preview against dark, light, or checkered backgrounds before downloading.</p>`,
    `<p>This ${escapeHtml(icon.style)} icon from ${escapeHtml(icon.library)} works well across <strong>${escapeHtml(catCtx)}</strong>. The ${escapeHtml(icon.style)} visual style is specifically suited for ${escapeHtml(styleU)}.</p><p class="muted">Customize it in IconStash: pick a color preset or enter any hex code, set exact dimensions, adjust stroke weight, then copy SVG code or download a PNG — no account needed.</p>`,
    `<p>Icons in the ${escapeHtml(icon.style)} style — like ${escapeHtml(icon.displayName)} — are designed for ${escapeHtml(styleU)}. Use it across <strong>${escapeHtml(catCtx)}</strong> for a consistent, professional look.</p><p class="muted">IconStash's editor lets you fine-tune color, size, and stroke width in real time, then export in the format that fits your workflow: SVG, PNG, JSX, or CSS background-mask.</p>`,
    `<p>The ${escapeHtml(icon.displayName)} icon (${escapeHtml(icon.library)}) is categorized under <strong>${escapeHtml(icon.category)}</strong>. Its ${escapeHtml(icon.style)} style is optimal for ${escapeHtml(styleU)} and scales cleanly from 16px to 512px.</p><p class="muted">Use the IconStash detail panel to preview with a custom background, adjust stroke width, and generate production-ready SVG or PNG files without any external tools.</p>`
  ];
  const useCardBody = useVariants[hx % useVariants.length];

  /* React code snippet */
  let codeBlock = "";
  if (libInfo && libInfo.reactCode) {
    try {
      const code = libInfo.reactCode(icon.name);
      codeBlock = `<pre><code>${escapeHtml(code)}</code></pre>`;
    } catch (e) {
      codeBlock = `<pre><code>npm install ${escapeHtml(libNpm)}</code></pre>`;
    }
  } else {
    codeBlock = `<pre><code>npm install ${escapeHtml(libNpm)}</code></pre>`;
  }

  /* SVG code snippet (escaped for display) */
  const svgForDisplay = escapeHtml(renderSvg(icon, 24));

  /* Related links */
  const relatedLinks = related.map((item) => `<li><a href="/icons/${item.slug}/">${escapeHtml(item.keyword)}</a></li>`).join("");
  const peopleAlso = related.slice().reverse().slice(0, 6).map((item) => `<a href="/icons/${item.slug}/">${escapeHtml(item.keyword)}</a>`).join("");

  /* Library info card */
  const libCardHtml = libInfo
    ? `<article class="card" itemscope itemtype="https://schema.org/SoftwareApplication">
      <h2>About <span itemprop="name">${escapeHtml(libInfo.fullName)}</span></h2>
      <p itemprop="description">${escapeHtml(libInfo.desc)}</p>
      <ul class="lib-meta">
        <li><strong>Total icons:</strong> ${escapeHtml(libInfo.count)}+</li>
        <li><strong>Style:</strong> ${escapeHtml(libInfo.style)}</li>
        <li><strong>License:</strong> ${escapeHtml(libInfo.license)}</li>
        <li><strong>npm package:</strong> <code>${escapeHtml(libInfo.npm)}</code></li>
      </ul>
      <a class="btn" href="${escapeHtml(libUrl)}" style="margin-top:12px;display:inline-block">Browse all ${escapeHtml(libInfo.count)} ${escapeHtml(libInfo.fullName)} icons →</a>
    </article>`
    : `<article class="card">
      <h2>About ${escapeHtml(icon.library)}</h2>
      <p>The ${escapeHtml(icon.library)} icon library is indexed in IconStash. Browse its full collection to find the right icon for your interface.</p>
      <a class="btn" href="${escapeHtml(libUrl)}" style="margin-top:12px;display:inline-block">Browse ${escapeHtml(icon.library)} icons →</a>
    </article>`;

  return `<!doctype html>
<html lang="en">
<head>
  <script async src="https://plausible.io/js/pa--bfaHBAPFGUV3yUn96sF4.js"></script>
  <script>window.plausible=window.plausible||function(){(plausible.q=plausible.q||[]).push(arguments)},plausible.init=plausible.init||function(i){plausible.o=i||{}};plausible.init()</script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escapeHtml(title)}</title>
  <meta name="description" content="${escapeHtml(description)}">
  <link rel="canonical" href="${escapeHtml(url)}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="${escapeHtml(title)}">
  <meta property="og:description" content="${escapeHtml(description)}">
  <meta property="og:url" content="${escapeHtml(url)}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="${escapeHtml(title)}">
  <meta name="twitter:description" content="${escapeHtml(description)}">
  <style>
    :root{color-scheme:dark;--bg:#07070d;--panel:#0f0f1c;--line:#1e1e32;--text:#f0f0ff;--muted:#8888aa;--blue:#2f80ff;--green:#00cc66}
    *{box-sizing:border-box;margin:0;padding:0}
    body{background:var(--bg);color:var(--text);font:15px/1.7 Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
    a{color:var(--blue);text-decoration:none}a:hover{text-decoration:underline}
    .wrap{max-width:980px;margin:0 auto;padding:32px 20px 72px}
    .crumbs{display:flex;gap:6px;flex-wrap:wrap;color:var(--muted);font-size:13px;margin-bottom:28px;align-items:center}
    .crumbs a{color:var(--muted)}.crumbs a:hover{color:var(--text)}
    .hero{display:grid;grid-template-columns:200px 1fr;gap:32px;align-items:center;margin-bottom:40px}
    .preview{height:200px;border:1px solid var(--line);border-radius:18px;background:var(--panel);display:grid;place-items:center;color:var(--blue)}
    h1{font-size:clamp(24px,4vw,44px);line-height:1.1;margin-bottom:14px;letter-spacing:-.02em;font-weight:800}
    .lead{color:var(--muted);font-size:16px;line-height:1.65;margin-bottom:20px}
    .cta{display:flex;gap:10px;flex-wrap:wrap}
    .btn{border:1px solid var(--line);border-radius:9px;padding:10px 16px;color:var(--text);background:var(--panel);font-size:14px;font-weight:600;cursor:pointer;display:inline-block}
    .btn.primary{background:var(--blue);border-color:var(--blue);color:#fff}
    .btn:hover{opacity:.88;text-decoration:none}
    .section-title{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin:40px 0 16px}
    .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}
    .grid.wide{grid-template-columns:1fr}
    .card{border:1px solid var(--line);background:var(--panel);border-radius:14px;padding:20px}
    .card h2{font-size:16px;font-weight:700;margin-bottom:10px;color:var(--text)}
    .card p{color:var(--muted);font-size:14px;line-height:1.65;margin-bottom:10px}
    .card p:last-child{margin-bottom:0}
    .card p.muted{color:#666688}
    .card strong{color:var(--text)}
    .card ul{padding-left:18px;color:var(--muted);font-size:14px}
    .card li{margin:4px 0}
    .card code{background:#0a0a18;border:1px solid var(--line);border-radius:4px;padding:1px 5px;font-size:12px;font-family:"JetBrains Mono",Consolas,monospace}
    .lib-meta{list-style:none;padding:0}
    .lib-meta li{display:flex;gap:8px;align-items:baseline;padding:4px 0;border-bottom:1px solid var(--line);font-size:13px}
    .lib-meta li:last-child{border-bottom:none}
    .lib-meta strong{color:var(--text);flex:0 0 120px}
    pre{background:#060610;border:1px solid var(--line);border-radius:10px;padding:16px;overflow-x:auto;margin-top:8px}
    pre code{font:500 12px/1.6 "JetBrains Mono",Consolas,monospace;color:#a8d8a8;white-space:pre}
    .chips{display:flex;gap:8px;flex-wrap:wrap;margin-top:4px}
    .chips a{border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:13px;color:var(--muted)}
    .chips a:hover{color:var(--text);border-color:#555;text-decoration:none}
    .faq-item{border-bottom:1px solid var(--line);padding:16px 0}
    .faq-item:last-child{border-bottom:none}
    .faq-item h3{font-size:15px;font-weight:700;color:var(--text);margin-bottom:8px}
    .faq-item p{color:var(--muted);font-size:14px;line-height:1.65}
    footer{margin-top:52px;padding-top:24px;border-top:1px solid var(--line);color:var(--muted);font-size:13px;display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;align-items:center}
    footer a{color:var(--muted)}footer a:hover{color:var(--text)}
    .footer-links{display:flex;gap:16px;flex-wrap:wrap}
    @media(max-width:680px){.hero{grid-template-columns:1fr}.preview{height:150px}}
  </style>
  <script type="application/ld+json">${JSON.stringify(schema).replace(/</g, "\\u003c")}</script>
</head>
<body>
<main class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb">
    <a href="/">IconStash</a><span>/</span>
    <a href="/#/library/${escapeHtml(icon.librarySlug)}">${escapeHtml(icon.library)}</a><span>/</span>
    <span>${escapeHtml(icon.displayName)}</span>
  </nav>

  <section class="hero">
    <div class="preview" aria-hidden="true">${renderSvg(icon, 100)}</div>
    <div>
      <h1>${escapeHtml(row.keyword)}</h1>
      <p class="lead">${escapeHtml(lead)}</p>
      <div class="cta">
        <a class="btn primary" href="${escapeHtml(appUrl)}">Open in editor</a>
        <a class="btn" href="${escapeHtml(libUrl)}">Browse ${escapeHtml(icon.library)}</a>
      </div>
    </div>
  </section>

  <p class="section-title">About this icon</p>
  <div class="grid">
    <article class="card">
      <h2>Use the ${escapeHtml(icon.displayName)} icon</h2>
      ${useCardBody}
    </article>
    <article class="card">
      <h2>Export formats</h2>
      <p>Copy clean SVG vectors with one click, generate custom-size PNG files from 16px to 512px, export JSX/React components ready to paste into your project, or use the icon as a CSS <code>background-mask</code> for flexible theming.</p>
      <p class="muted">All exports are based on the same editable vector — so the ${escapeHtml(icon.displayName)} icon stays pixel-perfect at 16px, 24px, 48px, and any large marketing size.</p>
    </article>
  </div>

  <p class="section-title">Use in your project</p>
  <div class="grid wide">
    <article class="card">
      <h2>React / npm — ${escapeHtml(icon.library)}</h2>
      ${codeBlock}
      <p class="muted" style="margin-top:12px">Copy the SVG markup directly from the IconStash editor to use the ${escapeHtml(icon.displayName)} icon without any npm package — paste it into HTML, JSX, or a design tool.</p>
      <h2 style="margin-top:18px">Inline SVG (copy &amp; paste)</h2>
      <pre><code>${svgForDisplay}</code></pre>
    </article>
  </div>

  <p class="section-title">Library &amp; related icons</p>
  <div class="grid">
    ${libCardHtml}
    <article class="card">
      <h2>Related searches</h2>
      <ul>${relatedLinks}</ul>
    </article>
  </div>

  <p class="section-title">People also search for</p>
  <div class="chips">${peopleAlso}</div>

  <p class="section-title">Frequently asked questions</p>
  <div class="card" style="padding:8px 20px">
    ${faq.map((item) => `<div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
      <h3 itemprop="name">${escapeHtml(item.q)}</h3>
      <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
        <p itemprop="text">${escapeHtml(item.a)}</p>
      </div>
    </div>`).join("")}
  </div>

  <footer>
    <span>© ${new Date().getFullYear()} <a href="/">IconStash.io</a> — 134,701 icons from 28 open-source libraries.</span>
    <div class="footer-links">
      <a href="/">Search icons</a>
      <a href="${escapeHtml(libUrl)}">${escapeHtml(icon.library)} icons</a>
      <a href="/seo/">HTML sitemap</a>
    </div>
  </footer>
</main>
</body>
</html>`;
}

/* ─── Write pages ─────────────────────────────────────────────────────────── */
function writePages(keywords, icons) {
  const byIcon = new Map(icons.map((icon) => [icon.id, icon]));
  console.log("Building index maps for related searches...");
  buildIndexes(keywords, byIcon);
  console.log("Indexes completed. Writing HTML files...");
  let count = 0;
  const total = keywords.length;
  const reportEvery = Math.round(total / 10) || 10000;
  for (const row of keywords) {
    const icon = byIcon.get(row.iconId);
    if (!icon) continue;
    const related = relatedFor(row, byIcon);
    const dir = path.join(OUT_DIR, row.slug);
    try { fs.mkdirSync(dir); } catch (err) { if (err.code !== "EEXIST") fs.mkdirSync(dir, { recursive: true }); }
    fs.writeFileSync(path.join(dir, "index.html"), pageHtml(row, icon, related));
    count++;
    if (count % reportEvery === 0) {
      console.log(`- Progress: ${Math.round((count / total) * 100)}% (${count.toLocaleString("en-US")} / ${total.toLocaleString("en-US")} written)`);
    }
  }
}

/* ─── Write sitemaps (unchanged) ─────────────────────────────────────────── */
function writeSitemaps(keywords) {
  const staticUrls = ["/", "/seo/"].concat(keywords.map((row) => row.url));
  const chunks = [];
  for (let i = 0; i < staticUrls.length; i += 50000) chunks.push(staticUrls.slice(i, i + 50000));
  chunks.forEach((chunk, index) => {
    const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${chunk.map((url) => `  <url><loc>${SITE_URL}${url}</loc><lastmod>${TODAY}</lastmod></url>`).join("\n")}\n</urlset>\n`;
    fs.writeFileSync(path.join(SITEMAP_DIR, `sitemap-${index + 1}.xml`), xml);
  });
  const indexXml = `<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${chunks.map((_, index) => `  <sitemap><loc>${SITE_URL}/sitemaps/sitemap-${index + 1}.xml</loc><lastmod>${TODAY}</lastmod></sitemap>`).join("\n")}\n</sitemapindex>\n`;
  fs.writeFileSync(path.join(ROOT, "sitemap.xml"), indexXml);
  fs.writeFileSync(path.join(ROOT, "robots.txt"), `User-agent: *\nAllow: /\n\nSitemap: ${SITE_URL}/sitemap.xml\n`);
}

/* ─── Write HTML sitemap (unchanged) ─────────────────────────────────────── */
function writeHtmlSitemap(keywords) {
  const perPage = 1000;
  const pages = [];
  for (let i = 0; i < keywords.length; i += perPage) pages.push(keywords.slice(i, i + perPage));
  const indexLinks = pages.map((_, index) => `<a href="/seo/sitemap-${index + 1}/">Sitemap ${index + 1}</a>`).join("");
  ensureDir(HTML_SITEMAP_DIR);
  fs.writeFileSync(path.join(HTML_SITEMAP_DIR, "index.html"), `<!doctype html><html lang="en"><head><script async src="https://plausible.io/js/pa--bfaHBAPFGUV3yUn96sF4.js"></script><script>window.plausible=window.plausible||function(){(plausible.q=plausible.q||[]).push(arguments)},plausible.init=plausible.init||function(i){plausible.o=i||{}};plausible.init()</script><meta charset="utf-8"><title>IconStash HTML Sitemap</title><meta name="description" content="Browse all ${keywords.length.toLocaleString("en-US")} IconStash icon landing pages."><style>body{font:15px/1.6 system-ui;margin:32px;background:#07070d;color:#f5f7fb}a{display:inline-block;margin:6px 10px 6px 0;color:#8ab4ff}</style></head><body><h1>IconStash HTML Sitemap</h1><p>${keywords.length.toLocaleString("en-US")} icon landing pages across 28 open-source libraries.</p>${indexLinks}</body></html>`);
  pages.forEach((chunk, index) => {
    const dir = path.join(HTML_SITEMAP_DIR, `sitemap-${index + 1}`);
    ensureDir(dir);
    const links = chunk.map((row) => `<li><a href="${row.url}">${escapeHtml(row.keyword)}</a></li>`).join("");
    fs.writeFileSync(path.join(dir, "index.html"), `<!doctype html><html lang="en"><head><script async src="https://plausible.io/js/pa--bfaHBAPFGUV3yUn96sF4.js"></script><script>window.plausible=window.plausible||function(){(plausible.q=plausible.q||[]).push(arguments)},plausible.init=plausible.init||function(i){plausible.o=i||{}};plausible.init()</script><meta charset="utf-8"><title>IconStash Sitemap ${index + 1}</title><meta name="description" content="IconStash icon pages ${index * perPage + 1}–${Math.min((index + 1) * perPage, keywords.length)}."><style>body{font:15px/1.6 system-ui;margin:32px;background:#07070d;color:#f5f7fb}a{color:#8ab4ff}li{margin:4px 0}</style></head><body><h1>IconStash Sitemap ${index + 1}</h1><ul>${links}</ul></body></html>`);
  });
}

/* ─── Main ────────────────────────────────────────────────────────────────── */
function main() {
  const index = readJson(path.join(DATA_DIR, "index.json"));
  const libraries = index.libraries || [];
  console.log(`Loading ${libraries.length} libraries...`);
  const icons = libraries.flatMap(normalizeLibrary).filter((icon) => icon.body && icon.base);
  console.log(`Loaded ${icons.length.toLocaleString("en-US")} icons.`);
  console.log(`Generating up to ${PAGE_LIMIT.toLocaleString("en-US")} keyword pages...`);
  const keywords = buildKeywords(icons);
  cleanOutput();
  fs.writeFileSync(KEYWORD_DB, JSON.stringify({
    generatedAt: new Date().toISOString(),
    siteUrl: SITE_URL,
    pageLimit: PAGE_LIMIT,
    totalKeywords: keywords.length,
    keywords
  }, null, 2));
  writePages(keywords, icons);
  writeSitemaps(keywords);
  writeHtmlSitemap(keywords);
  console.log(`\nGenerated ${keywords.length.toLocaleString("en-US")} pages.`);
  console.log(`Wrote ${path.relative(ROOT, KEYWORD_DB)}, sitemap.xml, robots.txt, and HTML sitemap.`);
}

main();
