# catalog
README.md

Интернет-дүкеннің тауар каталогын басқару жүйесі

Бұл жоба Python тілінде жасалған оқу жобасы. Мақсат — интернет-дүкеннің тауар каталогын басқару логикасын құру және келесі технологияларды тәжірибеде қолдану:
	•	Лексикалық және синтаксистік талдау (Lark)
	•	Тестілеу (pytest, TDD идеялары)
	•	CI/CD (GitHub Actions)
	•	Ерекшелік өңдеу және логтау
	•	UML диаграммалары мен SOLID принциптері
	•	REST API (Flask немесе FastAPI) арқылы жұмыс

⸻

Жоба құрылымы

catalog-project/

├─ app/
│  ├─ main.py         – REST API
│  ├─ service.py      – бизнес-логика
│  ├─ parser.py       – Lark парсері
│  ├─ models.py       – деректер модельдері
│  ├─ logger.py       – логтау және қателерді өңдеу
│
├─ tests/
│  ├─ test_parser.py  – парсерге арналған тесттер
│  ├─ test_api.py     – API тесттері
│
├─ .github/workflows/
│  ├─ ci.yml          – GitHub Actions конфигурациясы
│
├─ requirements.txt
├─ README.md
└─ UML.png            – UML диаграммасы


⸻

1. Лексикалық және синтаксистік талдау (Lark)

Жоба ішінде командаларды өңдеуге арналған шағын синтаксистік тіл қолданылады. Командалар мысалы:

SHOW products
FILTER price > 1000

parser.py файлы Lark кітапханасын пайдаланып, келесі грамматиканы іске асырады:

?start: command

?command: show_cmd
        | filter_cmd

show_cmd: "SHOW" ("products" | "category")
filter_cmd: "FILTER" "price" OP NUMBER

OP: ">" | "<" | ">=" | "<="
NUMBER: /\d+/

%import common.WS
%ignore WS

Парсер команданы өңдеп, оны Python dict форматына түрлендіреді.

⸻

2. API (main.py)

API Flask/FastAPI арқылы жүзеге асырылған. Негізгі мүмкіндіктер:
	•	Барлық өнімдерді шығару
	•	Жаңа өнім қосу
	•	Бағасы бойынша фильтр қолдану
	•	Парсер көмегімен командаларды API арқылы орындау

API бизнес-логикадан тәуелсіз болуы үшін барлық өңдеу service.py файлына бөлінген (SOLID: SRP).

⸻

3. Тестілеу (pytest)

Барлық тесттер tests/ каталогында.

Мысал тест:

def test_show_products():
    result = parse_command("SHOW products")
    assert result["type"] == "show"

API тесттері:

pytest


⸻

4. CI/CD (GitHub Actions)

.github/workflows/ci.yml файлында тесттер автоматты түрде орындалатын конфигурация бар.

name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.10
      - run: pip install -r requirements.txt
      - run: pytest

Репозиторийге push жасалған сайын тесттер автоматты түрде іске қосылады.

⸻

5. Ерекшелік өңдеу және логтау

logger.py ішінде стандартты Python logging жүйесі қолданылған.
API және парсер қателері лог файлға және консольге түседі.

Мысалы:

logger.error("Parser error: %s", message)


⸻

6. UML және SOLID

Жоба архитектурасы UML (UML.png) диаграммасында көрсетілген.

SOLID принциптері:
	•	SRP: API, сервис, парсер, логтау жеке модульдерге бөлінген
	•	OCP: жаңа командалар грамматикаға оңай қосылады
	•	LSP: модельдер өзара ауыстырылатындай жазылған
	•	ISP: модульдер артық функцияларға тәуелді емес
	•	DIP: API бизнес-логикаға тікелей тәуелді емес, service арқылы жұмыс істейді

⸻

7. Орнату және іске қосу

Тәуелділіктерді орнату:

pip install -r requirements.txt

API серверін іске қосу:

python app/main.py

Парсерді тексеру:

python app/parser.py

Тесттерді орындау:

pytest
