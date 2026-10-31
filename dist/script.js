/* Local illustration: no dependencies, trackers, remote requests, or simulated performance claims. */
const svgNS = 'http://www.w3.org/2000/svg';
const routes = document.querySelector('#routes');
const signal = document.querySelector('#signal');
const figure = document.querySelector('.system-figure');
const untangle = document.querySelector('#untangle');
const story = document.querySelector('#diagram-story');
const layerButtons = [...document.querySelectorAll('.diagram-layers button')];
const isUk = document.documentElement.lang === 'uk';

const connectedPaths = [
  'M45 215 C90 215 110 110 190 110',
  'M45 215 C90 215 110 320 190 320',
  'M190 110 C250 70 310 70 370 110',
  'M190 320 C250 360 310 360 370 320',
  'M190 320 C140 260 140 170 190 110',
  'M370 110 C370 180 370 250 370 320',
  'M190 110 C250 110 310 320 370 320',
  'M190 320 C250 320 310 110 370 110',
  'M370 110 C455 110 470 215 535 215',
  'M370 320 C455 320 470 215 535 215',
  'M535 215 C550 410 195 425 190 320',
  'M370 320 C330 230 230 200 190 110',
  'M370 110 C330 175 230 245 190 320',
  'M535 215 C545 20 195 15 190 110',
  'M45 215 C95 10 280 5 370 110',
  'M370 110 C310 160 250 160 190 110',
  'M190 110 C300 190 420 215 535 215'
];
const visibleConnections = new Set([0, 1, 2, 3, 5, 7, 9, 10, 11]);
const routeStates = connectedPaths.map((connected, index) => {
  const y = 72 + index * 22;
  const endY = 72 + ((index * 5 + 3) % 14) * 22;
  const bend = index % 2 === 0 ? 44 : 386;
  const tangled = `M45 ${y} C${180 + index * 9} ${bend} ${340 - index * 7} ${430 - bend} 535 ${endY}`;
  const path = document.createElementNS(svgNS, 'path');
  path.setAttribute('d', tangled);
  if (index === 10 || index === 11) path.classList.add('feedback-route');
  if (index >= 14) path.classList.add('removed-route');
  routes.append(path);
  return { path, tangled, connected, index };
});

const layers = isUk ? {
  processes: {
    title: 'Спрощення процесів',
    text: 'Прибрати зайві кроки та передачі завдань. Автоматизувати рутину, щоб люди зосередилися на рішеннях, де вони дійсно потрібні.',
    highlighted: [0, 2, 5, 9],
    signal: 'M45 215 C90 215 110 110 190 110 C250 70 310 70 370 110 C370 180 370 250 370 320 C455 320 470 215 535 215'
  },
  people: {
    title: 'Навчання людей. Об’єднання команд.',
    text: 'Показати людям, як працює система. Уточнити відповідальність, налагодити комунікацію та залучати зворотний зв’язок до спільних рішень.',
    highlighted: [1, 7, 5, 9],
    description: 'Маршрут «Люди» проходить послідовно: Контекст, Люди, Аналіз, Рішення та Результат. Інші залежності та зворотний зв’язок залишаються видимими.',
    signal: 'M45 215 C90 215 110 320 190 320 C250 320 310 110 370 110 C370 180 370 250 370 320 C455 320 470 215 535 215'
  },
  ai: {
    title: 'ШІ як екзоскелет',
    text: 'Підтримує аналіз, роботу зі знаннями та навчання людей. Допомагає швидко автоматизувати рутину й адаптувати щоденні процеси. Відповідальність за рішення залишається за людьми.',
    highlighted: [14, 5, 11, 16],
    visible: [14, 5, 11, 16, 3, 1, 12],
    dashed: [1, 12],
    influences: [3],
    description: 'Маршрут «ШІ» проходить через Контекст, Аналіз із підтримкою ШІ на цьому зв’язку, Рішення, Процеси та Результат. Люди впливають на Рішення через прямий суцільний зв’язок. Зв’язки від Контексту до Людей та від Аналізу до Людей — штрихові.',
    legend: 'Суцільні лінії показують основний маршрут і вплив людей на рішення. Штрихові лінії з’єднують контекст та аналіз із людьми.',
    signal: 'M45 215 C95 10 280 5 370 110 C370 180 370 250 370 320 C330 230 230 200 190 110 C300 190 420 215 535 215'
  }
} : {
  processes: {
    title: 'Simpler processes',
    text: 'Eliminate friction and unnecessary handoffs. Automate routine workflows so people can focus on the decisions that truly matter.',
    highlighted: [0, 2, 5, 9],
    signal: 'M45 215 C90 215 110 110 190 110 C250 70 310 70 370 110 C370 180 370 250 370 320 C455 320 470 215 535 215'
  },
  people: {
    title: 'Empowering people. Connecting teams.',
    text: 'Help people see how the whole system fits together. Clarify ownership, streamline communication, and feed real-world insights back into shared decisions.',
    highlighted: [1, 7, 5, 9],
    description: 'The People route flows through Context, People, Analysis, Decisions, and Outcome. Other dependencies and feedback loops remain visible.',
    signal: 'M45 215 C90 215 110 320 190 320 C250 320 310 110 370 110 C370 180 370 250 370 320 C455 320 470 215 535 215'
  },
  ai: {
    title: 'AI as an exoskeleton',
    text: 'Amplify analysis, knowledge work, and team enablement. Rapidly automate routine tasks and help processes adapt on the fly — while keeping humans firmly in charge of decisions.',
    highlighted: [14, 5, 11, 16],
    visible: [14, 5, 11, 16, 3, 1, 12],
    dashed: [1, 12],
    influences: [3],
    description: 'The AI route follows Context, AI-augmented Analysis, Decisions, Processes, and Outcome. People influence Decisions directly via a solid path, while Context and Analysis connect to People via dashed lines.',
    legend: 'Solid lines trace the primary flow and direct human influence on decisions. Dashed lines keep context and analysis connected to people.',
    signal: 'M45 215 C95 10 280 5 370 110 C370 180 370 250 370 320 C330 230 230 200 190 110 C300 190 420 215 535 215'
  }
};

let organized = false;
function selectLayer(name) {
  const layer = layers[name];
  figure.dataset.layer = name;
  layerButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.layer === name)));
  const visible = layer.visible ? new Set(layer.visible) : visibleConnections;
  const dashed = layer.dashed || [10, 11];
  routeStates.forEach(({ path, index }) => {
    path.classList.toggle('is-highlighted', organized && layer.highlighted.includes(index));
    path.classList.toggle('removed-route', organized ? !visible.has(index) && !layer.highlighted.includes(index) : index >= 14);
    path.classList.toggle('feedback-route', dashed.includes(index));
    path.classList.toggle('is-influence', organized && (layer.influences || []).includes(index));
  });
  if (organized) {
    signal.setAttribute('d', layer.signal);
    document.querySelector('#diagram-desc').textContent = layer.description || (isUk ? 'Пов’язаний граф з’єднує контекст із процесами та людьми, далі — аналіз, людські рішення та результат. Криволінійні та штрихові шляхи зворотного зв’язку залишаються.' : 'A connected graph links context to processes and people, then analysis, human decisions, and outcomes, with active feedback loops preserved.');
  }
  document.querySelector('#diagram-explanation h3').textContent = layer.title;
  document.querySelector('#diagram-explanation p').textContent = layer.text;
  document.querySelector('.graph-legend').textContent = layer.legend || (isUk ? 'Суцільні лінії показують залежності. Штрихові повертають зворотний зв’язок у роботу. Відповідальність за рішення залишається за людьми.' : 'Solid lines show dependencies. Dashed lines cycle feedback back into the loop. Decisions always remain in human hands.');
}

function setDiagram(nextState) {
  organized = nextState;
  untangle.setAttribute('aria-pressed', String(organized));
  figure.classList.toggle('organized', organized);
  story.hidden = !organized;
  routeStates.forEach(({ path, tangled, connected, index }) => {
    path.setAttribute('d', organized ? connected : tangled);
  });
  document.querySelector('#diagram-status').textContent = organized ? (isUk ? '02 / ПОВ’ЯЗАНА ТА АДАПТИВНА' : '02 / CONNECTED & ADAPTABLE') : (isUk ? '01 / ЗАПЛУТАНА РОБОТА' : '01 / TANGLED WORK');
  untangle.innerHTML = organized ? (isUk ? 'Показати заплутаність <span aria-hidden="true">↺</span>' : 'Show the tangle <span aria-hidden="true">↺</span>') : (isUk ? 'Подивитися зміни <span aria-hidden="true">↗</span>' : 'See what changes <span aria-hidden="true">↗</span>');
  document.querySelector('.figure-note').innerHTML = organized ? (isUk ? 'система, яку можна зрозуміти,<br>з якою можна працювати і яку можна змінювати.' : 'a system you can understand,<br>work with, and adapt.') : (isUk ? 'десь тут є корисна<br>система.' : 'there’s a useful system<br>in here somewhere.');
  document.querySelector('#diagram-desc').textContent = organized ? (isUk ? 'Пов’язаний граф з’єднує контекст із процесами та людьми, далі — аналіз, людські рішення та результат. Криволінійні та штрихові шляхи зворотного зв’язку зберігаються. Досліджуйте Процеси, Люди та ШІ для розуміння внеску кожного.' : 'A connected graph links context to processes and people, then analysis, human decisions, and outcomes. Curved and dashed feedback paths remain. Explore Processes, People, and AI to see how each contributes.') : (isUk ? 'Ілюстративна мережа ліній, що перетинаються. Натисніть «Подивитися зміни», щоб побачити процеси, людей, аналіз, людські рішення та зворотний зв’язок.' : 'An illustrative network of crossing lines. Choose See what changes to reveal processes, people, analysis, human decisions, and feedback.');
  selectLayer('processes');
  if (!organized) signal.setAttribute('d', 'M45 215 C170 15 425 405 535 215');
}

untangle.addEventListener('click', () => setDiagram(!organized));
layerButtons.forEach(button => button.addEventListener('click', () => selectLayer(button.dataset.layer)));

const copyButton = document.querySelector('#copy-profile');
copyButton.addEventListener('click', async () => {
  const url = 'https://www.linkedin.com/in/oleksandryukhno/';
  try {
    if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText(url);
    document.querySelector('#copy-status').textContent = isUk ? 'Скопійовано. До зустрічі.' : 'Copied. See you there.';
  } catch {
    document.querySelector('#copy-status').textContent = isUk ? 'Виділіть і скопіюйте посилання нижче.' : 'Select and copy the link below.';
    let fallback = document.querySelector('#profile-url');
    if (!fallback) {
      fallback = document.createElement('input');
      fallback.id = 'profile-url';
      fallback.setAttribute('aria-label', isUk ? 'Посилання на профіль для копіювання' : 'Profile URL to copy');
      fallback.readOnly = true;
      fallback.value = url;
      fallback.className = 'profile-url';
      copyButton.after(fallback);
    }
    fallback.focus();
    fallback.select();
  }
});

let scrollFrame = false;
function showProgress() {
  const distance = document.documentElement.scrollHeight - window.innerHeight;
  document.querySelector('.reading-line').style.width = `${distance > 0 ? Math.min(100, window.scrollY / distance * 100) : 0}%`;
  scrollFrame = false;
}
window.addEventListener('scroll', () => {
  if (!scrollFrame) { scrollFrame = true; requestAnimationFrame(showProgress); }
}, { passive: true });
window.addEventListener('resize', showProgress);
showProgress();

const langSwitch = document.querySelector('.lang-switch');
if (langSwitch) {
  langSwitch.addEventListener('click', (e) => {
    if (window.location.hash) {
      e.preventDefault();
      const target = langSwitch.getAttribute('href').split('#')[0];
      window.location.href = target + window.location.hash;
    }
  });
}
