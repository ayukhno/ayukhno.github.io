"""Builds the downloadable CV and the plain-text versions for AI systems.

One source of facts (CV below) produces, per language:
  dist/cv/cv-<lang>.md         plain Markdown CV, linked from llms.txt
  tools/cv/out/print-<lang>.html  print layout, rendered to PDF by render_pdf.sh
and dist/llms.txt for AI assistants and answer engines.

Keep these facts in sync with the CV pages: dist/index.html (English) and dist/uk-cv.html (Ukrainian).
Run: python3 tools/cv/build_cv.py && sh tools/cv/render_pdf.sh
"""

import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITE = "https://ayukhno.github.io/"
LINKEDIN = "https://www.linkedin.com/in/oleksandryukhno/"
GITHUB = "https://github.com/ayukhno"

CV = {
    "en": {
        "name": "Oleksandr Yukhno",
        "title": "Operational transformation · PMO and change management · AI in processes",
        "meta": [
            "Currently in Poland, from Ukraine · remote, hybrid, travel · open to relocation within Europe",
            f"LinkedIn: {LINKEDIN} · Website: {SITE}",
        ],
        "h_summary": "Summary",
        "summary": [
            "I see a company as a system where processes, technology and finance, together with employees and "
            "customers, have to work as one, and that is how I build change. For me, AI is a tool: an exoskeleton "
            "within this system.",
            "I can help companies that are changing and rebuilding their operations. I am looking for projects and "
            "roles in operational and AI transformation, where the PMO becomes the centre of change management and "
            "I am responsible for results.",
        ],
        "facts": [
            "30+ years in technology, projects and operations",
            "Ciklum, CTO: 50 → 250 people while I was there",
            "Silpo, IT and PMO Director: 120 → 300 stores, about 40,000 people",
            "Silpo, M&A: 5 acquisitions and large-scale restructurings; 20+ legal entities merged",
        ],
        "h_help": "Where I can help",
        "help": [
            ("Operations and the commercial side together in tools that drive financial results",
             "store P&L by the 5th of the following month; profitability of every product category in every store after all costs."),
            ("A balanced scorecard (BSC) that worked in practice",
             "goals cascaded from the C-level to every store; a weekly and monthly overall score for each store."),
            ("Workforce productivity, from the annual budget to yesterday’s plan vs. actual",
             "FTE calculated from planned revenue and processes; payroll targets met; a controlled impact on EBITDA."),
            ("Systemic change: acquisitions, restructurings and building a PMO",
             "built and led the PMO at Silpo; merged more than 20 legal entities into one."),
            ("The new challenge: systematic use of AI with a controlled payback",
             "rebuild how the company works together with people who already work with AI, and build “Digital Management”: "
             "a single, transparent system for running the company and making decisions."),
        ],
        "h_start": "First 100 days",
        "start": [
            ("Goals and direction", "where the company is going, its priorities and the direction of change."),
            ("Pain points and quick wins", "the most pressing problems and areas that can deliver quick, tangible results, so the start pays for itself right away."),
            ("Team, plan, delivery", "form the team, set goals and plans, coordinate and implement; with AI, each step goes much faster."),
            ("Scaling AI", "new solutions, help for each employee in daily work, or a company-wide system, depending on the company’s goals."),
        ],
        "h_exp": "Experience",
        "exp": [
            ("Applied AI", "Open hobby projects and a startup in development", "Now", None, [
                "Broad hands-on experience with AI outside corporate business. In 2026, my AI-based car-audio tuning method won five championship awards.",
                "Open projects built with AI: github.com/ayukhno/autosound-tuning-skill, github.com/ayukhno/autosound-tcc.",
                "Own AI systems, in progress: a digital project office; a personal/corporate AI assistant.",
            ]),
            ("Silpo", "Director of the Project Management Office (PMO), reporting to the Retail Director", "From 2012",
             "One of Ukraine’s largest food retail chains; while I worked there it grew from about 120 to 300 stores, with around 40,000 people.", [
                "PMO project portfolio in operations, commerce and IT, run by my team under my leadership, some managed by me: markdowns, single-source promotion management, a single product classification and assortment management, self-checkouts, expiry-date control, electronic document management.",
                "Acquisitions and restructurings: integrating acquired chains, moving stores between legal entities. Led 4 large-scale business transformation programmes.",
                "Balanced scorecard (BSC) from a single store to the whole chain.",
                "Annual planning of headcount (FTE), payroll and productivity for stores and production, based on planned revenue.",
                "Store P&L by the 5th of the following month; profitability of product categories in every store.",
                "A mobile platform for store processes; one annual stocktake instead of monthly ones.",
                "Projects with consultants: McKinsey (working group on operational processes), PwC (shared service centre for accounting), KPMG (setting up a procurement department).",
                "Designed and taught a project management course for retail.",
            ]),
            ("Silpo", "Director of the IT Office, reporting to the Executive Director", "2008–2012", None, [
                "More than 20 operating legal entities merged into one. Store process mapping and labour standards.",
                "Staff and checkout schedules planned from customer traffic. Standards and procedures for regional IT teams.",
            ]),
            ("Scanvaegt International", "Regional Manager, Eastern Europe", "2006–2007", None, [
                "Supply and implementation projects for industrial systems.",
            ]),
            ("Ciklum", "CTO", "2005–2006", None, [
                "IT infrastructure, standards, planning and budgeting while the company grew from about 50 to 250 people.",
            ]),
            ("Banking systems and projects", "", "1994–2005", None, [
                "Developer, team lead and project manager, chief engineer at Bank Ukraina, international account manager at ProFIX.",
            ]),
        ],
        "h_edu": "Education and professional development",
        "edu": [
            ("Kharkiv Technical School of Radio Electronics", "CNC machine tools", "1987–1991"),
            ("Kharkiv Polytechnic Institute", "Computer science, systems programming", "1991–1996"),
            ("MAUP", "Business management", "2002–2003"),
            ("McKinsey", "Training during the operations project at Silpo", ""),
            ("Ernst & Young", "Economics of management decisions: cost, profit, pricing", ""),
            ("IMD Business School", "Short executive programmes (in Lausanne and at other locations)", ""),
        ],
        "h_skills": "Skills",
        "skills": [
            ("Change management", "PMO, project portfolio, transformation programmes, acquisitions and restructurings."),
            ("Operations", "process mapping and redesign, labour standards, workforce (FTE) and payroll planning."),
            ("Finance and metrics", "P&L, budgeting, cost allocation, BSC and KPIs from a single store to the whole chain."),
            ("Technology", "IT infrastructure and standards, mobile solutions for processes, AI with several models, cross-checks and data security controls."),
            ("People", "mentoring and training project managers, working one-to-one."),
        ],
        "h_qual": "Personal qualities",
        "qual": [
            "I run several complex projects at once and implement change so that the business keeps running without interruption.",
            "I judge every change by whether it can be scaled and how much it will save the company.",
            "I speak directly, rely on facts and stay calm under pressure.",
            "I keep learning and bring proven approaches from other companies and industries.",
            "I mentor project managers and share my experience.",
            "I deliberately build speed and flexibility: small steps and frequent iterations in the startup and my own AI projects.",
        ],
        "qual_note": "The first five points are confirmed by Spencer Stuart, Hogan, Gallup and 360-degree assessments.",
        "h_lang": "Languages",
        "lang": "Ukrainian, English (professional working proficiency)",
        "h_contact": "Contact",
        "contact": [f"LinkedIn: {LINKEDIN}", f"GitHub: {GITHUB}", f"Website: {SITE}"],
    },
    "uk": {
        "name": "Олександр Юхно",
        "title": "Операційна трансформація · PMO і управління змінами · ШІ в процесах",
        "meta": [
            "Зараз у Польщі, родом з України · віддалено, гібрид, відрядження · готовий до переїзду в межах Європи",
            f"LinkedIn: {LINKEDIN} · Сайт: {SITE}uk-cv.html",
        ],
        "h_summary": "Коротко",
        "summary": [
            "Вмію бачити компанію як систему, де процеси, технології та фінанси у взаємодії зі співробітниками й "
            "клієнтами мають працювати разом, і саме так будую зміни. ШІ для мене — інструмент, екзоскелет у цій системі.",
            "Можу бути корисним компаніям, які змінюються і перебудовують операції. Шукаю проєкти й ролі в операційній "
            "та ШІ-трансформації, де PMO стає центром управління змінами, а я відповідаю за результат.",
        ],
        "facts": [
            "30+ років у технологіях, проєктах та операціях",
            "Ciklum, CTO: 50 → 250 людей за час моєї роботи",
            "Сільпо, директор ІТ і PMO: 120 → 300 магазинів, близько 40 000 людей",
            "Сільпо, M&A: 5 поглинань і реструктуризацій великого масштабу; об’єднано понад 20 юросіб",
        ],
        "h_help": "Де можу бути корисним",
        "help": [
            ("Операції й комерція як інструменти впливу на фінансовий результат",
             "P&L магазину до 5-го числа наступного місяця; прибутковість кожної товарної категорії в кожному магазині після всіх витрат."),
            ("Збалансована система показників (BSC), яка запрацювала в реальності",
             "каскадування цілей від C-level до кожного магазину; щотижнева й щомісячна зведена оцінка магазину."),
            ("Продуктивність персоналу: від річного бюджету до план-факту за вчора",
             "FTE від планового виторгу й процесів; виконання цілей з ФОП; контрольований вплив на EBITDA."),
            ("Системні зміни: поглинання, реструктуризації та побудова PMO",
             "побудував і очолив PMO у Сільпо; об’єднав понад 20 юросіб в одну."),
            ("Новий виклик: системне застосування ШІ з контрольованою окупністю",
             "перебудовувати роботу компанії разом із людьми, які вже вміють працювати з ШІ, і будувати «Цифровий менеджмент»: "
             "єдину прозору систему керування та ухвалення рішень."),
        ],
        "h_start": "Перші 100 днів",
        "start": [
            ("Цілі та напрям", "куди рухається компанія, її пріоритети й напрям змін."),
            ("Больові точки та швидкі результати", "найболючіші проблеми й ділянки зі швидким відчутним ефектом, щоб старт одразу себе окупив."),
            ("Команда, план, реалізація", "сформувати команду, цілі й плани, координувати та впроваджувати; з ШІ кожен крок іде значно швидше."),
            ("Масштабування ШІ", "нові рішення, допомога кожному працівникові або загальнокорпоративна система — залежно від цілей компанії."),
        ],
        "h_exp": "Досвід",
        "exp": [
            ("Прикладний ШІ", "Відкриті хобі-проєкти та стартап, який зараз у розробці", "Зараз", None, [
                "Широкий досвід з ШІ поза корпоративним бізнесом. Метод налаштування автозвуку з ШІ у 2026 році приніс п’ять нагород на чемпіонатах.",
                "Відкриті проєкти, побудовані з ШІ: github.com/ayukhno/autosound-tuning-skill, github.com/ayukhno/autosound-tcc.",
                "Власні системи з ШІ, у роботі: цифровий проєктний офіс; персональний/корпоративний ШІ-асистент.",
            ]),
            ("Сільпо", "Директор офісу управління проєктами (PMO), у підпорядкуванні ритейл-директора", "З 2012",
             "Одна з найбільших продуктових мереж України; за час моєї роботи мережа зросла приблизно зі 120 до 300 магазинів, близько 40 000 людей.", [
                "Портфель проєктів PMO в операціях, комерції та ІТ: вела моя команда під моїм керівництвом, частину я вів сам. Серед них: уцінка, акції в єдиному джерелі, єдиний класифікатор товарів і управління асортиментом, каси самообслуговування, контроль термінів придатності, електронний документообіг.",
                "Поглинання й реструктуризації: інтеграція куплених мереж, переведення магазинів між юрособами. Вів 4 масштабні програми трансформації бізнесу.",
                "Збалансована система показників (BSC) від магазину до всієї мережі.",
                "Річне планування чисельності персоналу (FTE), фонду оплати праці й продуктивності магазинів і виробництва від планового виторгу.",
                "P&L магазинів до 5-го числа наступного місяця; прибутковість товарних категорій у кожному магазині.",
                "Мобільна платформа для процесів у магазинах; переоблік раз на рік замість щомісячного.",
                "Проєкти з консультантами: McKinsey (робоча група з операційних процесів), PwC (спільний центр обслуговування для бухгалтерії), KPMG (створення відділу закупівель).",
                "Розробив і викладав курс з управління проєктами для ритейлу.",
            ]),
            ("Сільпо", "Директор ІТ-офісу, у підпорядкуванні виконавчого директора", "2008–2012", None, [
                "Об’єднання понад 20 операційних юросіб в одну. Опис процесів магазинів і нормативи праці.",
                "Планування графіків персоналу й кас за трафіком покупців. Стандарти й процедури для регіональних ІТ-команд.",
            ]),
            ("Scanvaegt International", "Регіональний менеджер у Східній Європі", "2006–2007", None, [
                "Проєкти постачання й впровадження промислових систем.",
            ]),
            ("Ciklum", "CTO", "2005–2006", None, [
                "ІТ-інфраструктура, стандарти, планування й бюджетування, поки компанія зростала приблизно з 50 до 250 людей.",
            ]),
            ("Банківські системи і проєкти", "", "1994–2005", None, [
                "Розробник, керівник групи та проєктів, головний інженер у Банку «Україна», менеджер з міжнародних клієнтів у ProFIX.",
            ]),
        ],
        "h_edu": "Освіта та професійний розвиток",
        "edu": [
            ("Харківський технікум радіоелектроніки", "Верстати з ЧПК", "1987–1991"),
            ("Харківський політехнічний інститут", "Комп’ютерні науки, системне програмування", "1991–1996"),
            ("МАУП", "Управління бізнесом", "2002–2003"),
            ("McKinsey", "Тренінги під час операційного проєкту в Сільпо", ""),
            ("Ernst & Young", "Економіка управлінських рішень: собівартість, прибуток, ціноутворення", ""),
            ("Бізнес-школа IMD", "Короткі бізнес-програми (у Лозанні та виїзні)", ""),
        ],
        "h_skills": "Навички",
        "skills": [
            ("Управління змінами", "PMO, портфель проєктів, програми трансформації, поглинання й реструктуризації."),
            ("Операції", "опис і перебудова процесів, нормування праці, планування персоналу (FTE) і ФОП."),
            ("Фінанси й показники", "P&L, бюджетування, алокація витрат, BSC і KPI від магазину до мережі."),
            ("Технології", "ІТ-інфраструктура й стандарти, мобільні рішення для процесів, ШІ з кількома моделями, перевіркою й контролем безпеки даних."),
            ("Люди", "наставництво й навчання керівників проєктів, робота один на один."),
        ],
        "h_qual": "Особисті якості",
        "qual": [
            "Веду кілька складних проєктів одночасно й упроваджую зміни так, щоб бізнес працював без зупинок.",
            "Оцінюю кожну зміну за тим, чи її можна тиражувати і скільки вона заощадить компанії.",
            "Говорю прямо, спираюся на факти, спокійний під тиском.",
            "Постійно вчуся і переношу вдалі підходи з інших компаній і галузей.",
            "Наставляю керівників проєктів і ділюся досвідом.",
            "Свідомо розвиваю швидкість і гнучкість: малі кроки й часті ітерації в стартапі та власних ШІ-проєктах.",
        ],
        "qual_note": "Перші п’ять пунктів підтверджено оцінками Spencer Stuart, Hogan, Gallup та 360.",
        "h_lang": "Мови",
        "lang": "українська, англійська — робоча",
        "h_contact": "Контакти",
        "contact": [f"LinkedIn: {LINKEDIN}", f"GitHub: {GITHUB}", f"Сайт: {SITE}uk-cv.html"],
    },
}


def markdown(c):
    out = [f"# {c['name']}", "", c["title"], ""]
    out += [f"- {m}" for m in c["meta"]] + ["", f"## {c['h_summary']}", ""]
    out += [p + "\n" for p in c["summary"]] + [f"- {f}" for f in c["facts"]] + [""]
    out += [f"## {c['h_help']}", ""] + [f"- **{h}:** {t}" for h, t in c["help"]] + [""]
    out += [f"## {c['h_start']}", ""] + [f"{i}. **{h}:** {t}" for i, (h, t) in enumerate(c["start"], 1)] + [""]
    out += [f"## {c['h_exp']}", ""]
    for org, role, when, note, bullets in c["exp"]:
        out += [f"### {org}" + (f": {role}" if role else "") + f" ({when})", ""]
        if note:
            out += [note, ""]
        out += [f"- {b}" for b in bullets] + [""]
    out += [f"## {c['h_edu']}", ""]
    out += [f"- {org}: {what}" + (f" ({when})" if when else "") for org, what, when in c["edu"]] + [""]
    out += [f"## {c['h_skills']}", ""] + [f"- **{h}:** {t}" for h, t in c["skills"]] + [""]
    out += [f"## {c['h_qual']}", ""] + [f"- {q}" for q in c["qual"]] + ["", f"*{c['qual_note']}*", ""]
    out += [f"## {c['h_lang']}", "", c["lang"], "", f"## {c['h_contact']}", ""] + [f"- {x}" for x in c["contact"]] + [""]
    return "\n".join(out)


def print_html(c, lang):
    e = html.escape
    parts = [f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{e(c['name'])} — CV</title>
<style>
  @page {{ size: A4; margin: 12mm 14mm 12mm 14mm; }}
  body {{ font: 10pt/1.36 -apple-system, "Helvetica Neue", Arial, sans-serif; color: #111; margin: 0; }}
  h1 {{ font-size: 19pt; margin: 0; letter-spacing: -0.01em; }}
  .title {{ font-size: 10.5pt; margin: 1pt 0 4pt; color: #1f45c9; font-weight: 600; }}
  .meta {{ margin: 0 0 2pt; padding: 0; list-style: none; color: #333; font-size: 9.4pt; }}
  h2 {{ font-size: 10pt; text-transform: uppercase; letter-spacing: 0.06em; color: #1f45c9; border-bottom: 1px solid #c9ccd4; padding-bottom: 1.5pt; margin: 8pt 0 4pt; break-after: avoid; }}
  p {{ margin: 0 0 3pt; }}
  ul, ol {{ margin: 1pt 0 4pt 13pt; padding: 0; }}
  li {{ margin: 0 0 1.5pt; break-inside: avoid; }}
  .facts {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1pt 14pt; list-style: none; margin: 3pt 0 0; padding: 0; font-size: 9.4pt; }}
  .facts li::before {{ content: "▪ "; color: #1f45c9; }}
  .cols {{ columns: 2; column-gap: 16pt; }}
  .job {{ margin-bottom: 4pt; }}
  .job-head {{ display: flex; justify-content: space-between; gap: 12pt; font-weight: 700; break-after: avoid; }}
  .job-head span:last-child {{ white-space: nowrap; font-weight: 400; color: #333; }}
  .org {{ color: #333; font-weight: 600; }}
  .note {{ color: #333; font-style: italic; margin: 0.5pt 0 1pt; }}
  .edu {{ display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: repeat(3, auto); grid-auto-flow: column; gap: 1.5pt 16pt; }}
  .row span:last-child {{ color: #333; }}
  .small {{ font-size: 9pt; color: #444; font-style: italic; }}
</style>
</head>
<body>
<h1>{e(c['name'])}</h1>
<div class="title">{e(c['title'])}</div>
<ul class="meta">""" + "".join(f"<li>{e(m)}</li>" for m in c["meta"]) + f"""</ul>
<h2>{e(c['h_summary'])}</h2>
""" + "".join(f"<p>{e(p)}</p>" for p in c["summary"]) + """
<ul class="facts">""" + "".join(f"<li>{e(f)}</li>" for f in c["facts"]) + f"""</ul>
<h2>{e(c['h_help'])}</h2>
<ol>""" + "".join(f"<li><b>{e(h)}:</b> {e(t)}</li>" for h, t in c["help"]) + f"""</ol>
<h2>{e(c['h_start'])}</h2>
<ol>""" + "".join(f"<li><b>{e(h)}:</b> {e(t)}</li>" for h, t in c["start"]) + f"""</ol>
<h2>{e(c['h_exp'])}</h2>
"""]
    for org, role, when, note, bullets in c["exp"]:
        role_html = f" · {e(role)}" if role else ""
        parts.append(f'<div class="job"><div class="job-head"><span><span class="org">{e(org)}</span>{role_html}</span><span>{e(when)}</span></div>')
        if note:
            parts.append(f'<p class="note">{e(note)}</p>')
        if bullets:
            parts.append("<ul>" + "".join(f"<li>{e(b)}</li>" for b in bullets) + "</ul>")
        parts.append("</div>\n")
    parts.append(f"<h2>{e(c['h_edu'])}</h2>\n<div class=\"edu\">")
    for org, what, when in c["edu"]:
        parts.append(f'<div class="row"><span><b>{e(org)}</b>: {e(what)}</span>' + (f"<span> · {e(when)}</span>" if when else "") + "</div>")
    parts.append("</div>\n")
    parts.append(f"<h2>{e(c['h_skills'])}</h2><ul>" + "".join(f"<li><b>{e(h)}:</b> {e(t)}</li>" for h, t in c["skills"]) + "</ul>\n")
    parts.append(f"<h2>{e(c['h_qual'])}</h2><ul class=\"cols\">" + "".join(f"<li>{e(q)}</li>" for q in c["qual"]) + f"</ul><p class=\"small\">{e(c['qual_note'])}</p>\n")
    parts.append(f"<h2>{e(c['h_lang'])} · {e(c['h_contact'])}</h2><p>{e(c['lang'])}</p><p>{e(' · '.join(c['contact']))}</p>\n</body>\n</html>\n")
    return "".join(parts)


def llms_txt():
    en = CV["en"]
    summary = " ".join(en["summary"])
    return f"""# {en['name']}

> {en['title']}. {summary}

Online CV in English and Ukrainian, in two views: a short CV and a fuller Story. Contact via LinkedIn only.

## CV

- [CV in English (web)]({SITE}): where I can help, first 100 days, experience, education, skills
- [CV in Ukrainian (web)]({SITE}uk-cv.html): the same content in Ukrainian
- [Story in English (web)]({SITE}story.html): the CV with more depth, career story and AI projects
- [Story in Ukrainian (web)]({SITE}uk.html): the same content in Ukrainian
- [CV in English (Markdown)]({SITE}cv/cv-en.md): plain text version for AI systems
- [CV in Ukrainian (Markdown)]({SITE}cv/cv-uk.md): plain text version for AI systems
- [CV in English (PDF)]({SITE}cv/Oleksandr-Yukhno-CV-EN.pdf)
- [CV in Ukrainian (PDF)]({SITE}cv/Oleksandr-Yukhno-CV-UA.pdf)

## Projects

- [Autosound Tuning Skill](https://github.com/ayukhno/autosound-tuning-skill): a deterministic seven-phase process for car-audio DSP tuning, with AI flexible at every step
- [Autosound TCC](https://github.com/ayukhno/autosound-tcc): multilingual desktop app for macOS and Windows on top of the skill
- [This website](https://github.com/ayukhno/ayukhno.github.io): built with Claude, Codex and Gemini; the direction and the check of every line are mine

## Contact

- [LinkedIn]({LINKEDIN})
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
