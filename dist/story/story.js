// Highlight the current chapter in the side rail and the current section in the top bar.
(() => {
  if (!("IntersectionObserver" in window)) return;

  const watch = (targets, links, margin) => {
    const byId = new Map(links.map((a) => [a.getAttribute("href").slice(1), a]));
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        links.forEach((a) => a.removeAttribute("aria-current"));
        const link = byId.get(entry.target.id);
        if (link) link.setAttribute("aria-current", "true");
      });
    }, { rootMargin: margin });
    targets.forEach((t) => observer.observe(t));
  };

  const railLinks = [...document.querySelectorAll(".rail a")];
  watch([...document.querySelectorAll(".chapter")], railLinks, "-35% 0px -60% 0px");

  const navLinks = [...document.querySelectorAll(".topnav a")];
  const sections = navLinks.map((a) => document.querySelector(a.getAttribute("href"))).filter(Boolean);
  watch(sections, navLinks, "-40% 0px -55% 0px");
})();
