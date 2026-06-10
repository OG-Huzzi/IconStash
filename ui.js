(function () {
  const toasts = new Set();

  function qs(selector, root = document) {
    return root.querySelector(selector);
  }

  function qsa(selector, root = document) {
    return Array.from(root.querySelectorAll(selector));
  }

  function toast(message, type = "info", duration = 3200) {
    const container = qs("#toast-container");
    if (!container) return;
    const node = document.createElement("div");
    node.className = `toast toast-${type}`;
    node.style.setProperty("--toast-ms", `${duration}ms`);
    const label = document.createElement("span");
    label.textContent = message;
    node.appendChild(label);
    container.appendChild(node);
    toasts.add(node);
    setTimeout(() => {
      node.classList.add("exiting");
      setTimeout(() => {
        toasts.delete(node);
        node.remove();
      }, 220);
    }, duration);
  }

  function openModal(id) {
    const modal = qs(`#${id}`);
    const backdrop = qs("#modal-backdrop");
    if (!modal || !backdrop) return;
    qsa(".modal").forEach((entry) => entry.classList.add("hidden"));
    backdrop.classList.remove("hidden");
    modal.classList.remove("hidden");
  }

  function closeModals() {
    qsa(".modal").forEach((entry) => entry.classList.add("hidden"));
    qs("#modal-backdrop")?.classList.add("hidden");
    qs("#compare-toggle")?.classList.remove("active");
  }

  function particleBurst(target) {
    if (!target) return;
    const rect = target.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    for (let i = 0; i < 6; i += 1) {
      const dot = document.createElement("i");
      const angle = (Math.PI * 2 * i) / 6;
      dot.className = "particle";
      dot.style.left = `${cx}px`;
      dot.style.top = `${cy}px`;
      dot.style.background = i % 2 ? "var(--neon-pink)" : "var(--neon-blue)";
      dot.style.setProperty("--tx", `${Math.cos(angle) * 42}px`);
      dot.style.setProperty("--ty", `${Math.sin(angle) * 42}px`);
      document.body.appendChild(dot);
      setTimeout(() => dot.remove(), 520);
    }
  }

  function successButton(button, label = "Copied!") {
    if (!button) return;
    const old = button.textContent;
    button.classList.add("copy-success");
    button.textContent = label;
    particleBurst(button);
    setTimeout(() => {
      button.classList.remove("copy-success");
      button.textContent = old;
    }, 1500);
  }

  function animateNumber(element, target, duration = 700) {
    if (!element) return;
    const start = Number(String(element.textContent || "0").replace(/,/g, "")) || 0;
    const end = Number(target) || 0;
    const started = performance.now();
    element.classList.remove("number-pop");
    void element.offsetWidth;
    element.classList.add("number-pop");
    function frame(now) {
      const t = Math.min(1, (now - started) / duration);
      const eased = t === 1 ? 1 : 1 - Math.pow(2, -10 * t);
      const value = Math.round(start + (end - start) * eased);
      element.textContent = value.toLocaleString("en-US");
      if (t < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  function setupModalClosers() {
    qsa(".modal-close, #modal-backdrop").forEach((node) => {
      node.addEventListener("click", closeModals);
    });
  }

  function setupStatsObserver() {
    const stats = qs("#stats-bar");
    if (!stats) return;
    const run = () => {
      qsa(".stat-num", stats).forEach((node) => animateNumber(node, Number(node.dataset.target || 0), 1500));
    };
    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver((entries) => {
        if (entries.some((entry) => entry.isIntersecting)) {
          run();
          observer.disconnect();
        }
      }, { threshold: 0.3 });
      observer.observe(stats);
    } else {
      run();
    }
  }

  function setupNetworkGate() {
    const gate = qs("#network-gate");
    if (gate) gate.classList.add("hidden");
    const retry = qs("#network-retry");
    retry?.addEventListener("click", () => {
      gate?.classList.add("hidden");
      toast("IconStash core files are bundled locally", "info");
    });
  }

  function createSkeletonRows(container, rows = 4, cols = 8) {
    if (!container) return;
    const html = Array.from({ length: rows }, (_, row) => (
      `<div class="virtual-row icons-row" style="--cols:${cols};height:var(--card-row-height);animation-delay:${row * 30}ms">` +
      Array.from({ length: cols }, () => `
        <div class="icon-card skeleton-card">
          <div class="skeleton-icon-placeholder"></div>
          <div class="skeleton-text-placeholder"></div>
        </div>
      `).join("") +
      "</div>"
    )).join("");
    container.innerHTML = html;
  }

  function init() {
    setupModalClosers();
    setupStatsObserver();
    setupNetworkGate();
  }

  window.IconStashUI = {
    qs,
    qsa,
    toast,
    openModal,
    closeModals,
    particleBurst,
    successButton,
    animateNumber,
    createSkeletonRows,
    init
  };
})();
