// Footer year
document.getElementById('y').textContent = new Date().getFullYear();

// Theme toggle (persist)
const root = document.documentElement;
const themeToggle = document.getElementById('themeToggle');
if (localStorage.getItem('theme') === 'dark') root.classList.add('dark');
themeToggle.addEventListener('click', () => {
  root.classList.toggle('dark');
  localStorage.setItem('theme', root.classList.contains('dark') ? 'dark' : 'light');
});

// Mobile nav
const navToggle = document.getElementById('navToggle');
const navList = document.getElementById('navList');
navToggle?.addEventListener('click', () => {
  const open = navList.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(open));
});

// Projects
const PROJECTS = [
  { title: "Animal Faces Recognition", desc: "Cat/Dog face recognition — Data Mining & Machine Learning project.", tags: ["Python", "ML", "CV"], link: "https://github.com/ATemova/face-recog-cat-dog" },
  { title: "BookFlow", desc: "Systems III course project — book management flow.", tags: ["Java", "Backend", "Course"], link: "https://github.com/ATemova/sys3-project" },
  { title: "KeepTrack", desc: "Management Information Technology course — tracking application.", tags: ["Full-stack", "Course"], link: "https://github.com/zstoimchev/KeepTrack/tree/main" },
  { title: "FAMNIT Hackathon 3.0", desc: "University of Primorska hackathon — 4-person team.", tags: ["Hackathon", "Team"], link: "https://github.com/ATemova/FAMNIT-Hackathon-3.0" },
  { title: "DragonHack", desc: "24h hackathon — 4-person team project.", tags: ["Hackathon", "Team"], link: "https://github.com/christymanthara/Dragonborn" },
  { title: "Heat Simulator", desc: "Programming III course — heat simulation project.", tags: ["Java", "Simulation", "Course"], link: "https://github.com/ATemova/Programming-III-Project-Heat-Simulation" }
];

const grid = document.getElementById('projectGrid');
const filterInput = document.getElementById('filter');

function render(items) {
  grid.innerHTML = items.map(p => `
    <li class="project">
      <h3>${p.title}</h3>
      <p>${p.desc}</p>
      <div class="meta">${(p.tags || []).map(t => `<span class="tag">${t}</span>`).join('')}</div>
      <div><a class="btn ghost" target="_blank" rel="noopener" href="${p.link}">View</a></div>
    </li>
  `).join('');
}

function applyFilter() {
  const q = (filterInput.value || '').toLowerCase().trim();
  const items = q
    ? PROJECTS.filter(p =>
        p.title.toLowerCase().includes(q) ||
        p.desc.toLowerCase().includes(q) ||
        (p.tags || []).some(t => t.toLowerCase().includes(q))
      )
    : PROJECTS;
  render(items);
}

render(PROJECTS);
filterInput?.addEventListener('input', applyFilter);

// Contact form toast (no network)
document.querySelector('.contact-form')?.addEventListener('submit', (e) => {
  e.preventDefault();
  const btn = e.target.querySelector('button[type="submit"]');
  const old = btn.textContent;
  btn.disabled = true; btn.textContent = 'Sending...';
  setTimeout(() => {
    btn.disabled = false; btn.textContent = old;
    toast('Thanks! Your (demo) message was captured locally.');
    e.target.reset();
  }, 700);
});

function toast(msg){
  const el = document.createElement('div');
  el.textContent = msg;
  Object.assign(el.style, {
    position:'fixed', left:'50%', bottom:'24px', transform:'translateX(-50%)',
    padding:'10px 14px', borderRadius:'10px', background:'var(--card)',
    border:'1px solid var(--border)', boxShadow:'var(--shadow)', zIndex:9999
  });
  document.body.appendChild(el);
  setTimeout(()=> el.remove(), 2000);
}