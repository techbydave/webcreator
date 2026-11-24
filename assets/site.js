/* WebCreator by TechByDave: shared page script (home + about).
   Every feature checks that its elements exist, so one file serves both pages. */
{
const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
$$(".year").forEach((el) => (el.textContent = new Date().getFullYear()));

/* ---------- split headings into words that rise from a mask ---------- */
function splitWords(el) {
  const walk = (node) => {
    [...node.childNodes].forEach((n) => {
      if (n.nodeType === 3) {
        const frag = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach((part) => {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.append(part); return; }
          const w = document.createElement("span"); w.className = "wd";
          const inner = document.createElement("span"); inner.textContent = part;
          w.append(inner); frag.append(w);
        });
        n.replaceWith(frag);
      } else if (n.nodeType === 1 && !n.classList.contains("wd")) walk(n);
    });
  };
  walk(el);
  $$(".wd>span", el).forEach((s, i) => (s.style.transitionDelay = `${i * 55}ms`));
}
$$("h2").forEach((h) => { h.classList.add("split"); splitWords(h); });

/* ---------- statement that lights up word by word ---------- */
$$(".say").forEach((el) => {
  const walk = (node) => [...node.childNodes].forEach((n) => {
    if (n.nodeType === 3) {
      const frag = document.createDocumentFragment();
      n.textContent.split(/(\s+)/).forEach((p) => { if (!p) return; if (/^\s+$/.test(p)) frag.append(p); else { const s = document.createElement("span"); s.className = "sw"; s.textContent = p; frag.append(s); } });
      n.replaceWith(frag);
    } else if (n.nodeType === 1) walk(n);
  });
  walk(el);
});

/* ---------- reveal on scroll ---------- */
const reveal = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); reveal.unobserve(e.target); } }), { threshold: .15 });
$$(".rv").forEach((el) => {
  const p = el.parentElement;
  if (p.matches(".bento,.plans,.work,.steps,.values,.mission")) el.style.transitionDelay = `${([...p.children].indexOf(el) % 4) * 100}ms`;
  reveal.observe(el);
});
const headWatch = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); headWatch.unobserve(e.target); } }), { threshold: .3 });
$$("h2.split").forEach((h) => headWatch.observe(h));
if (reduced) $$(".rv,.split").forEach((el) => el.classList.add("in"));

/* ---------- counters ---------- */
const counter = new IntersectionObserver((es) => es.forEach((e) => {
  if (!e.isIntersecting) return; counter.unobserve(e.target);
  const el = e.target, to = Number(el.dataset.count), suffix = el.dataset.suffix || "";
  if (reduced) { el.textContent = to + suffix; return; }
  const t0 = performance.now();
  const step = (t) => { const k = Math.min(1, (t - t0) / 1400); el.textContent = Math.round(to * (1 - (1 - k) ** 3)) + suffix; if (k < 1) requestAnimationFrame(step); };
  requestAnimationFrame(step);
}), { threshold: .6 });
$$("[data-count]").forEach((el) => counter.observe(el));

/* ---------- one scroll loop for every scroll-driven effect ---------- */
const root = document.documentElement;
const frame = $(".frame"), pnav = $(".pnav"), hz = $(".hz"), rail = $(".hz .rail"), story = $(".story");
const rows = $$(".rows .r"), pars = $$(".par"), says = $$(".say");
const navLinks = $$(".pnav a.l[href^='#']");
const sections = navLinks.map((a) => document.querySelector(a.getAttribute("href"))).filter(Boolean);
let ticking = false;
function onScroll() {
  ticking = false;
  const y = scrollY, vh = innerHeight;
  root.style.setProperty("--sp", clamp(y / (root.scrollHeight - vh)));
  if (frame) {
    const h = frame.offsetHeight;
    frame.style.setProperty("--hp", reduced ? 0 : clamp(y / h).toFixed(3));
    pnav && pnav.classList.toggle("show", y > h * .7);
  }
  if (!reduced) {
    rows.forEach((r, i) => { const dir = i % 2 ? 1 : -1; r.style.transform = `translateX(${(dir * y * .25) - (i % 2 ? 600 : 0)}px)`; });
    pars.forEach((el) => { const r = el.getBoundingClientRect(), mid = r.top + r.height / 2 - vh / 2; el.style.transform = `translateY(${mid * -(Number(el.dataset.speed) || .06)}px)`; });
  }
  says.forEach((el) => {
    const r = el.getBoundingClientRect(), words = el._w || (el._w = $$(".sw", el));
    const p = reduced ? 1 : clamp((vh * .85 - r.top) / (r.height + vh * .35));
    const n = Math.round(p * words.length);
    words.forEach((w, i) => w.classList.toggle("lit", i < n));
  });
  if (hz && rail && innerWidth > 760 && !reduced) {
    const r = hz.getBoundingClientRect(), total = hz.offsetHeight - vh;
    const p = clamp(-r.top / total), dist = rail.scrollWidth - innerWidth;
    rail.style.transform = `translateX(${-p * Math.max(0, dist)}px)`;
    hz.style.setProperty("--hzp", p.toFixed(3));
  }
  if (story) {
    const r = story.getBoundingClientRect();
    story.style.setProperty("--stp", reduced ? 1 : clamp((vh * .6 - r.top) / r.height).toFixed(3));
  }
  if (sections.length) {
    let cur = null;
    sections.forEach((s) => { if (s.getBoundingClientRect().top < vh * .45) cur = s.id; });
    navLinks.forEach((a) => a.classList.toggle("on", a.getAttribute("href") === "#" + cur));
  }
}
const requestTick = () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } };
addEventListener("scroll", requestTick, { passive: true });
addEventListener("resize", requestTick);
onScroll();

/* ---------- home hero: example sites on the phone ---------- */
const site = $("#site");
if (site) {
  const scenes = [
    { name: "Agape Counselling", bg: "#16312d", img: "radial-gradient(circle at 30% 30%,#8fd3c0,#3f8a7a 45%,#1c3f39)", h: "Healing starts at home.", p: "Individual, couple and family counselling.", btn: "#e9f3ef", ink: "#16312d", cta: "Book a session", t: "Appointment approved", s: "Thu · 2:00 pm · In person" },
    { name: "Bloom Studio", bg: "#2b1720", img: "radial-gradient(circle at 70% 30%,#ffd1dc,#c06c84 45%,#5b2a3a)", h: "Hair that feels like you.", p: "Cuts, colour and braids by appointment.", btn: "#ffd1dc", ink: "#2b1720", cta: "Book a chair", t: "New booking request", s: "Sat · 11:30 am · Colour" },
    { name: "Spotless Co.", bg: "#0e2340", img: "radial-gradient(circle at 40% 30%,#bfe1ff,#4f86ff 45%,#123a7a)", h: "Your home, sparkling.", p: "Weekly and deep cleans across the GTA.", btn: "#ffffff", ink: "#0e2340", cta: "Get a quote", t: "Quote request received", s: "3-bedroom · Deep clean" },
  ];
  const toast = $("#toast");
  let scene = 0, toastTimer = 0, auto = 0;
  const paint = (i) => {
    const s = scenes[i];
    site.style.background = s.bg;
    site.innerHTML = `<div class="top"><span></span><i></i></div><div class="heroimg"></div><h5></h5><p></p><div class="book"></div><div class="chips"><span></span><span></span><span></span></div>`;
    $(".top span", site).textContent = s.name; $(".heroimg", site).style.background = s.img;
    $("h5", site).textContent = s.h; $("p", site).textContent = s.p;
    const b = $(".book", site); b.textContent = s.cta; b.style.background = s.btn; b.style.color = s.ink;
    $("#toast-t").textContent = s.t; $("#toast-s").textContent = s.s;
  };
  const showToast = (d) => { toast.classList.remove("show"); clearTimeout(toastTimer); toastTimer = setTimeout(() => toast.classList.add("show"), d); };
  const next = () => {
    scene = (scene + 1) % scenes.length; site.classList.add("out"); toast.classList.remove("show");
    setTimeout(() => { paint(scene); site.classList.remove("out"); showToast(700); }, reduced ? 0 : 420);
  };
  const restartAuto = () => { clearInterval(auto); if (!reduced) auto = setInterval(next, 6500); };
  paint(0);
  $("#next")?.addEventListener("click", () => { next(); restartAuto(); });
  const days = $("#days");
  setTimeout(() => {
    document.body.classList.add("landed"); showToast(1000); restartAuto();
    if (days && !reduced) {
      const unit = days.querySelector("small").outerHTML, t0 = performance.now();
      const step = (t) => { const k = Math.min(1, (t - t0) / 1200); days.innerHTML = Math.round(14 * (1 - (1 - k) ** 3)) + unit; if (k < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    }
  }, reduced ? 0 : 1700);
  const float = $("#float");
  if (float && frame && !reduced && matchMedia("(pointer:fine)").matches) {
    frame.addEventListener("pointermove", (e) => {
      const r = frame.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, yy = (e.clientY - r.top) / r.height - .5;
      float.style.transform = `rotateY(${x * 14}deg) rotateX(${-yy * 10}deg) translate3d(${x * 14}px,${yy * 10}px,0)`;
    });
    frame.addEventListener("pointerleave", () => (float.style.transform = ""));
  }
} else {
  setTimeout(() => document.body.classList.add("landed"), reduced ? 0 : 300);
}

/* ---------- small interactions ---------- */
$$(".tile").forEach((t) => t.addEventListener("pointermove", (e) => { const r = t.getBoundingClientRect(); t.style.setProperty("--mx", `${e.clientX - r.left}px`); t.style.setProperty("--my", `${e.clientY - r.top}px`); }));
$$(".approve").forEach((b) => b.addEventListener("click", () => { const d = !b.classList.contains("done"); b.classList.toggle("done", d); b.textContent = d ? "Approved" : "Approve"; }));

const rank = $("#rank");
if (rank) {
  const climb = new IntersectionObserver((es) => es.forEach((e) => {
    if (!e.isIntersecting) return; climb.disconnect();
    const r = $$("div", rank), you = r[2], h = r[0].getBoundingClientRect().height + 8;
    setTimeout(() => {
      you.style.transform = `translateY(${-2 * h}px)`; r[0].style.transform = r[1].style.transform = `translateY(${h}px)`;
      $("b", you).textContent = "01"; $("b", r[0]).textContent = "02"; $("b", r[1]).textContent = "03";
    }, reduced ? 0 : 800);
  }), { threshold: .6 });
  climb.observe(rank);
}

const box = $("#faqs");
if (box && !box.children.length) {
  const faqs = [
    ["Do I need to know anything about tech?", "No. I set everything up and show you how your dashboard works in a short call. If you can use email, you can use it."],
    ["What do I need to give you to start?", "Your business name, logo (or I can design one), the services you offer, your hours and contact details, and any photos you have. I'll send a short checklist."],
    ["Do I own my website?", "Yes. The domain is registered in your name, and the site, content and designs are yours."],
    ["I already have a website. Can you redesign it?", "Yes. I keep what works, move your content over, and make sure your Google listing points to the new site."],
    ["Are there monthly costs?", "Only what the providers charge you directly for your domain and email account. Hosting is free, and the Care Plan is optional."],
    ["How do appointments work?", "Clients pick a time on your website. You get the request in your dashboard and by email, then approve or decline it with one tap. They're emailed automatically."],
    ["Do you work with businesses outside Toronto?", "Yes. Everything is done online, by video call and email."],
  ];
  box.innerHTML = faqs.map(([q, a], i) => `<div class="q glass"><button type="button" aria-expanded="false" aria-controls="a${i}">${q}<i aria-hidden="true"></i></button><div class="a" id="a${i}"><div><p>${a}</p></div></div></div>`).join("");
}
$$(".faq").forEach((f) => f.addEventListener("click", (e) => { const b = e.target.closest("button"); if (!b) return; const q = b.parentElement, open = !q.classList.contains("open"); q.classList.toggle("open", open); b.setAttribute("aria-expanded", String(open)); }));

$$("[data-plan]").forEach((a) => a.addEventListener("click", () => { const p = $("#p"); if (p) p.value = a.dataset.plan; }));

const quote = $("#quote");
quote?.addEventListener("submit", (e) => {
  e.preventDefault(); const f = e.target, err = $("#err");
  if (!f.name.value.trim()) { err.textContent = "Please add your name."; f.name.focus(); return; }
  if (!f.business.value.trim()) { err.textContent = "Please add your business name."; f.business.focus(); return; }
  err.textContent = "";
  const body = `Name: ${f.name.value}\nBusiness: ${f.business.value}\nPlan: ${f.plan.value}\n\n${f.message.value}`;
  location.href = `mailto:dave@techbydave.com?subject=${encodeURIComponent("Website quote: " + f.business.value)}&body=${encodeURIComponent(body)}`;
});
}
