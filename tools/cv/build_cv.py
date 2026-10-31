"""Builds the downloadable CV and the plain-text versions for AI systems.

One source of facts (CV below) produces, per language:
  dist/cv/cv-<lang>.md         plain Markdown CV, linked from llms.txt
  tools/cv/out/print-<lang>.html  print layout, rendered to PDF by render_pdf.sh
and dist/llms.txt for AI assistants and answer engines.

Keep these facts in sync with dist/index.html and dist/en.html.
Run: python3 tools/cv/build_cv.py && sh tools/cv/render_pdf.sh
"""

import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITE = "https://ayukhno.github.io/"
LINKEDIN = "https://www.linkedin.com/in/oleksandryukhno/"

CV = {
    "en": {
        "name": "Oleksandr Yukhno",
        "title": "AI Transformation · Next-generation PMO · Operational Transformation",
        "meta": [
            "Based in Poland · open to relocation within Europe · remote, hybrid, travel",
            f"LinkedIn: {LINKEDIN}",
            f"Website: {SITE}en.html",
        ],
        "h_summary": "Summary",
        "summary": (
            "30+ years across electronics, software, project delivery and retail operations. "
            "Former CTO at Ciklum and Director of the IT office and the project management office "
            "at Silpo, one of Ukraine's largest food retail chains (about 120 → 300 stores, "
            "around 40,000 people during my years). Today a partner at FlipManager, an AI-products "
            "startup, building AI assistants and an AI-run project office. Interested in projects and "
            "roles in AI adoption, operational transformation and building a next-generation PMO, "
            "where I own the result."
        ),
        "h_skills": "Core skills",
        "skills": [
            "AI adoption with governance: multi-vendor review, human decision, data-security readiness",
            "PMO set-up and portfolio management; training project managers",
            "Operational transformation and process redesign; labour standards and scheduling",
            "Planning, budgeting, store P&L, KPI systems (balanced scorecard)",
            "Restructuring: legal-entity mergers, integration of acquired chains",
            "IT infrastructure, standards and procedures; working across operations, commerce, finance and IT",
        ],
        "h_exp": "Experience",
        "exp": [
            ("FlipManager", "Partner (co-founder), AI-products startup", "Now", [
                "Two-partner startup building an AI exoskeleton for managers: four products on one base (DPA personal assistant, DBA small-business assistant, DPC corporate assistant, DCC Digital Company Compass).",
                "Lead the personal and small-business assistants; designing PMO Hub, an AI-run project office with fixed AI roles (product owner, architect, tester, design critic, auditor) and cross-checks by a second AI vendor.",
                "PMO Hub's prototype built hub-kit (the DPA base) and both public Autosound projects in 2026.",
            ]),
            ("Autosound (own projects, public on GitHub)", "Author", "2026", [
                "Claude skill that turns AI into a deterministic seven-phase process for tuning a car's sound processor from real measurements; 120+ releases since June 2026.",
                "TCC: multilingual desktop app for macOS and Windows on top of the skill; 4,300+ automated tests; works with different AI models directly or through OMP.",
                "Results in 2026: five awards for my own car at EMMA and AYA championships; a user's car took first place at the AYA Finale.",
            ]),
            ("Silpo", "Director of the Project Management Office (reporting to the COO)", "From 2012", [
                "Annual planning and budgeting of store and production headcount, payroll and productivity, driven by format, processes and planned revenue.",
                "Store P&L: the costs a store manager controls became visible by the 5th of the following month.",
                "KPI system based on the balanced scorecard, from a single store to the whole chain.",
                "Restructuring: legal-entity mergers, stores moved between entities, acquired chains integrated.",
                "Expert in a McKinsey working group on operational processes; projects on promotions, pricing, markdowns and assortment; mobile platform for store processes; one annual stocktake instead of monthly ones.",
                "Built and taught a practical project management course for retail.",
            ]),
            ("Silpo", "Director of the IT Office (reporting to the executive director)", "2008–2012", [
                "Standards, checklists and procedures for regional IT teams supporting the stores.",
                "Store processes described; document flow between stores and offices put in order, with a new records department.",
                "Labour standards; staff and checkout schedules planned in half-hour slots from customer traffic; queue alerts by SMS.",
                "More than 20 operating legal entities merged into one.",
            ]),
            ("Scanvaegt International", "Regional Manager, Eastern Europe (outstaffed from Ciklum)", "2006–2007", [
                "Industrial weighing and processing systems: equipment supply, commissioning and hardware and software roll-outs while large plants were being built, including the MHP slaughter plant in Kaniv.",
            ]),
            ("Ciklum", "CTO", "2005–2006", [
                "IT infrastructure, standards and procedures, planning and budgeting, presale and hiring support for clients.",
                "The company grew from about 50 to 250 people while I was there.",
            ]),
            ("ProFIX", "Project Manager, then Manager for International Clients", "2002–2005", [
                "Management of banking software projects and international client accounts.",
            ]),
            ("ProFIX", "Banking software", "1999–2002", [
                "Developing and delivering banking systems.",
            ]),
            ("Bank Ukraina", "Chief Engineer, Main Settlement Centre", "1998–1999", []),
            ("Avan", "Team Lead and Project Manager, banking automation", "1996–1998", []),
            ("Escape", "Software Developer (software for banks from 1995)", "1994–1996", []),
        ],
        "h_edu": "Education",
        "edu": [
            ("MAUP", "Business management", "2002–2003"),
            ("Kharkiv Polytechnic Institute", "Computer science, systems programming", "1991–1996"),
            ("Kharkiv Technical School of Radio Electronics", "CNC machine tools", "1987–1991"),
        ],
        "h_train": "Training",
        "train": [
            ("IMD Business School", "Short executive programmes (in Lausanne and on-site)", ""),
            ("Ernst & Young", "Decision management: cost, profit, pricing", "2013"),
            ("McKinsey", "Trainings during the operations project at Silpo", ""),
        ],
        "h_lang": "Languages",
        "lang": "Ukrainian (native), English (working)",
        "h_other": "Also",
        "footer": "P.S. AI assembled this file from my website, which I built together with AI: the idea on Wednesday, two days of thinking and a prototype with Codex, then eight hours with Claude building and Gemini reviewing and translating, to a proofread site online, for about $40 of AI usage. I set the direction and checked every line: the same way I would run AI projects in your company.",
        "other": "Built my own house and designed its engineering systems; the house and my apartment run as smart homes on a Raspberry Pi server with Home Assistant, now maintained and developed by AI.",
    },
    "uk": {
        "name": "Олександр Юхно",
        "title": "ШІ-трансформація · PMO нового покоління · Операційна трансформація",
        "meta": [
            "Базуюся в Польщі · відкритий до релокації в Європі · віддалено, гібрид, відрядження",
            f"LinkedIn: {LINKEDIN}",
            f"Сайт: {SITE}",
        ],
        "h_summary": "Коротко",
        "summary": (
            "Понад 30 років в електроніці, розробці ПЗ, управлінні проєктами та операціях ритейлу. "
            "Був CTO в Ciklum, директором ІТ-офісу та офісу управління проєктами в «Сільпо», одній "
            "із найбільших продуктових мереж України (приблизно 120 → 300 магазинів, близько 40 000 "
            "людей за час моєї роботи). Сьогодні партнер у FlipManager, стартапі ШІ-продуктів: створюю "
            "ШІ-асистентів і проєктний офіс, де значну частину роботи виконує ШІ. Цікавлять проєкти й "
            "ролі з упровадження ШІ, операційної трансформації та побудови PMO нового покоління, де я "
            "відповідаю за результат."
        ),
        "h_skills": "Ключові компетенції",
        "skills": [
            "Упровадження ШІ за правилами: перевірка іншим постачальником ШІ, рішення за людиною, готовність безпеки даних",
            "Побудова PMO та управління портфелем проєктів; навчання керівників проєктів",
            "Операційна трансформація та перепроєктування процесів; нормування праці й планування графіків",
            "Планування, бюджетування, P&L магазинів, системи KPI (збалансована система показників)",
            "Реструктуризація: об'єднання юросіб, інтеграція куплених мереж",
            "ІТ-інфраструктура, стандарти й процедури; спільна мова з операціями, комерцією, фінансами та ІТ",
        ],
        "h_exp": "Досвід",
        "exp": [
            ("FlipManager", "Партнер (співзасновник), стартап ШІ-продуктів", "Зараз", [
                "Стартап двох партнерів, що створює ШІ-екзоскелет для керівників: чотири продукти на одній основі (DPA персональний асистент, DBA асистент для малого бізнесу, DPC корпоративний асистент, DCC Digital Company Compass).",
                "Веду асистентів для людини та малого бізнесу; проєктую PMO Hub — проєктний офіс із чіткими ролями ШІ (власник продукту, архітектор, тестувальник, дизайн-критик, аудитор) і перевіркою іншим постачальником ШІ.",
                "На прототипі PMO Hub у 2026 році створено hub-kit (основу DPA) і обидва публічні проєкти Autosound.",
            ]),
            ("Autosound (власні проєкти, публічні на GitHub)", "Автор", "2026", [
                "Скіл для Claude, що перетворює ШІ на детерміновану систему із семи фаз для налаштування автомобільного звукового процесора за реальними замірами; понад 120 релізів з червня 2026 року.",
                "TCC: багатомовна настільна програма для macOS і Windows поверх скіла; понад 4 300 автотестів; працює з різними моделями ШІ напряму або через OMP.",
                "Результати 2026 року: п'ять нагород для мого авто на чемпіонатах EMMA та AYA; авто користувача посіло перше місце на фіналі AYA.",
            ]),
            ("«Сільпо»", "Директор офісу управління проєктами (у підпорядкуванні операційного директора)", "З 2012", [
                "Річне планування та бюджетування чисельності, фонду оплати праці й продуктивності магазинів і виробництва від формату, процесів і планового виторгу.",
                "P&L магазинів: витрати, на які впливає керуючий, стали доступні до 5-го числа наступного місяця.",
                "Система KPI на основі збалансованої системи показників, від магазину до всієї мережі.",
                "Реструктуризація: об'єднання юросіб, переведення магазинів між юрособами, інтеграція куплених мереж.",
                "Експерт у робочій групі McKinsey з операційних процесів; проєкти з акцій, цін, уцінки та асортименту; мобільна платформа для процесів магазинів; переоблік раз на рік замість щомісячних.",
                "Розробив і викладав практичний курс з управління проєктами для ритейлу.",
            ]),
            ("«Сільпо»", "Директор ІТ-офісу (у підпорядкуванні виконавчого директора)", "2008–2012", [
                "Стандарти, чеклісти та процедури для регіональних ІТ-команд, що підтримують магазини.",
                "Описані процеси магазинів; упорядкований документообіг між магазинами та офісами, створений відділ діловодства.",
                "Нормативи праці; графіки персоналу та кас півгодинними інтервалами за трафіком покупців; сповіщення про черги через SMS.",
                "Об'єднання понад 20 операційних юросіб в одну.",
            ]),
            ("Scanvaegt International", "Регіональний менеджер у Східній Європі (аутстаф від Ciklum)", "2006–2007", [
                "Промислові системи зважування та переробки: постачання обладнання, пусконалагодження, впровадження апаратних і програмних комплексів під час будівництва великих підприємств, зокрема забійного комплексу МХП у Каневі.",
            ]),
            ("Ciklum", "CTO", "2005–2006", [
                "ІТ-інфраструктура, стандарти й процедури, планування та бюджетування, підтримка пресейлу й найму для клієнтів.",
                "За час моєї роботи компанія зросла приблизно з 50 до 250 людей.",
            ]),
            ("ProFIX", "Керівник проєктів, згодом менеджер з роботи з міжнародними клієнтами", "2002–2005", [
                "Управління проєктами банківського ПЗ і роботою з міжнародними клієнтами.",
            ]),
            ("ProFIX", "Програми для банків", "1999–2002", [
                "Розробка та впровадження банківських систем.",
            ]),
            ("Банк «Україна»", "Головний інженер головного розрахункового центру", "1998–1999", []),
            ("Avan", "Керівник групи та проєктів, банківська автоматизація", "1996–1998", []),
            ("Escape", "Розробник ПЗ (з 1995 року програми для банків)", "1994–1996", []),
        ],
        "h_edu": "Освіта",
        "edu": [
            ("МАУП", "Управління бізнесом", "2002–2003"),
            ("Харківський політехнічний інститут", "Комп'ютерні науки, системне програмування", "1991–1996"),
            ("Харківський технікум радіоелектроніки", "Верстати з ЧПК", "1987–1991"),
        ],
        "h_train": "Тренінги",
        "train": [
            ("Бізнес-школа IMD", "Короткі бізнес-програми (у Лозанні та виїзні)", ""),
            ("Ernst & Young", "Економіка управлінських рішень: собівартість, прибуток, ціноутворення", "2013"),
            ("McKinsey", "Тренінги під час операційного проєкту в «Сільпо»", ""),
        ],
        "h_lang": "Мови",
        "lang": "українська (рідна), англійська (робоча)",
        "h_other": "Також",
        "footer": "P.S. Цей файл зібрав ШІ на основі мого сайту, який я створив разом із ШІ: задум у середу, два дні роздумів і прототип з Codex, потім вісім годин, де Claude будував, а Gemini критикував і перекладав, — і вичитаний сайт онлайн приблизно за $40 на ШІ. Напрям і перевірка кожного рядка — мої. Так само я вестиму ШІ-проєкти у вашій компанії.",
        "other": "Збудував власний дім і спроєктував його інженерні системи; будинок і квартира працюють за системою «розумний дім» на сервері Raspberry Pi з Home Assistant, який тепер підтримує й розвиває ШІ.",
    },
}


def markdown(c):
    out = [f"# {c['name']}", "", c["title"], ""]
    out += [f"- {m}" for m in c["meta"]] + ["", f"## {c['h_summary']}", "", c["summary"], ""]
    out += [f"## {c['h_skills']}", ""] + [f"- {s}" for s in c["skills"]] + ["", f"## {c['h_exp']}", ""]
    for org, role, when, bullets in c["exp"]:
        out += [f"### {role} — {org} ({when})", ""] + [f"- {b}" for b in bullets]
        out += [""]
    for key, head in (("edu", "h_edu"), ("train", "h_train")):
        out += [f"## {c[head]}", ""]
        out += [f"- {org}: {what}" + (f" ({when})" if when else "") for org, what, when in c[key]]
        out += [""]
    out += [f"## {c['h_lang']}", "", c["lang"], "", f"## {c['h_other']}", "", c["other"], "", "---", "", f"*{c['footer']}*", ""]
    return "\n".join(out)


def print_html(c, lang):
    e = html.escape
    parts = [f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{e(c['name'])} — CV</title>
<style>
  @page {{ size: A4; margin: 14mm 15mm 14mm 15mm; }}
  body {{ font: 9.6pt/1.38 -apple-system, "Helvetica Neue", Arial, sans-serif; color: #111; margin: 0; }}
  h1 {{ font-size: 20pt; margin: 0; letter-spacing: -0.01em; }}
  .title {{ font-size: 11pt; margin: 2pt 0 6pt; color: #1f45c9; font-weight: 600; }}
  .meta {{ margin: 0 0 4pt; padding: 0; list-style: none; color: #333; font-size: 9pt; }}
  h2 {{ font-size: 11pt; text-transform: uppercase; letter-spacing: 0.06em; color: #1f45c9; border-bottom: 1px solid #c9ccd4; padding-bottom: 2pt; margin: 10pt 0 5pt; break-after: avoid; }}
  p {{ margin: 0 0 4pt; }}
  ul {{ margin: 2pt 0 6pt 14pt; padding: 0; }}
  li {{ margin: 0 0 2pt; }}
  .job {{ break-inside: avoid; margin-bottom: 6pt; }}
  .job-head {{ display: flex; justify-content: space-between; gap: 12pt; font-weight: 700; }}
  .job-head span:last-child {{ white-space: nowrap; font-weight: 400; color: #333; }}
  .org {{ color: #333; font-weight: 600; }}
  .row {{ display: flex; justify-content: space-between; gap: 12pt; }}
  .row span:last-child {{ white-space: nowrap; color: #333; }}
  .footer {{ margin-top: 12pt; font-size: 8.6pt; color: #444; font-style: italic; }}
</style>
</head>
<body>
<h1>{e(c['name'])}</h1>
<div class="title">{e(c['title'])}</div>
<ul class="meta">""" + "".join(f"<li>{e(m)}</li>" for m in c["meta"]) + f"""</ul>
<h2>{e(c['h_summary'])}</h2>
<p>{e(c['summary'])}</p>
<h2>{e(c['h_skills'])}</h2>
<ul>""" + "".join(f"<li>{e(s)}</li>" for s in c["skills"]) + f"""</ul>
<h2>{e(c['h_exp'])}</h2>
"""]
    for org, role, when, bullets in c["exp"]:
        parts.append(f'<div class="job"><div class="job-head"><span>{e(role)} · <span class="org">{e(org)}</span></span><span>{e(when)}</span></div>')
        if bullets:
            parts.append("<ul>" + "".join(f"<li>{e(b)}</li>" for b in bullets) + "</ul>")
        parts.append("</div>\n")
    for key, head in (("edu", "h_edu"), ("train", "h_train")):
        parts.append(f"<h2>{e(c[head])}</h2>\n")
        for org, what, when in c[key]:
            parts.append(f'<div class="row"><span><b>{e(org)}</b> — {e(what)}</span><span>{e(when)}</span></div>\n')
    parts.append(f"<h2>{e(c['h_lang'])}</h2><p>{e(c['lang'])}</p>\n<h2>{e(c['h_other'])}</h2><p>{e(c['other'])}</p>\n<p class='footer'>{e(c['footer'])}</p>\n</body>\n</html>\n")
    return "".join(parts)


def llms_txt():
    en = CV["en"]
    return f"""# {en['name']}

> {en['summary']}

Online CV in English and Ukrainian. Contact via LinkedIn only.

## CV

- [CV in English (web)]({SITE}en.html): what I can help with, career story, AI projects, first 100 days
- [CV in Ukrainian (web)]({SITE}): the same content in Ukrainian
- [CV in English (Markdown)]({SITE}cv/cv-en.md): plain text version for AI systems
- [CV in Ukrainian (Markdown)]({SITE}cv/cv-uk.md): plain text version for AI systems
- [CV in English (PDF)]({SITE}cv/Oleksandr-Yukhno-CV-EN.pdf)
- [CV in Ukrainian (PDF)]({SITE}cv/Oleksandr-Yukhno-CV-UA.pdf)

## Projects

- [Autosound Tuning Skill](https://github.com/ayukhno/autosound-tuning-skill): AI as a deterministic seven-phase process for car-audio DSP tuning
- [Autosound TCC](https://github.com/ayukhno/autosound-tcc): multilingual desktop app for macOS and Windows on top of the skill
- [This website](https://github.com/ayukhno/ayukhno.github.io): an idea on Wednesday, a Codex prototype, then eight hours with Claude and Gemini to a proofread site online, about $40 of AI usage

## Contact

- [LinkedIn]({LINKEDIN})

*{en['footer']}*
"""


def main():
    out_dir = ROOT / "tools" / "cv" / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    cv_dir = ROOT / "dist" / "cv"
    cv_dir.mkdir(parents=True, exist_ok=True)
    for lang, c in CV.items():
        (cv_dir / f"cv-{lang}.md").write_text(markdown(c), encoding="utf-8")
        (out_dir / f"print-{lang}.html").write_text(print_html(c, lang), encoding="utf-8")
    (ROOT / "dist" / "llms.txt").write_text(llms_txt(), encoding="utf-8")
    print("built: dist/cv/cv-en.md, dist/cv/cv-uk.md, dist/llms.txt, tools/cv/out/print-*.html")


if __name__ == "__main__":
    main()
