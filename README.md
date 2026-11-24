# Warehouse Stock Tracker

Django веб-қосымшасы: қоймадағы тауарларды тіркеу және азайған қорды бақылау.

## Мүмкіндіктері
- Тауар атауын, ағымдағы санын және ең аз қор мөлшерін тіркеу.
- Қор мөлшері шекке тең немесе одан аз болса, **«Қор аз»** белгісін көрсету.
- Тауарларды тізімнен көру және жою.
- INFO журналы: тауар сәтті тіркелгенде.
- WARNING журналы: қор аз болғанда немесе форма тексеруден өтпегенде.
- `.env` арқылы жергілікті конфигурация; Render үшін PostgreSQL `DATABASE_URL`.
- WhiteNoise арқылы статикалық файлдарды беру.

## 1. Жергілікті іске қосу

Python 3.10+ орнатыңыз. Терминалда осы буманы ашыңыз:

```bash
python -m venv .venv
```

Windows:
```powershell
.venv\\Scripts\\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Тәуелділіктер:
```bash
python -m pip install -r requirements.txt
```

`.env` файлын `.env` деп көшіріңіз. `.env` ішіндегі `SECRET_KEY` орнына жаңа кілт қойыңыз:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Миграция және іске қосу:
```bash
python manage.py migrate
python manage.py runserver
```

Браузер: http://127.0.0.1:8000/

## 2. Журналды тексеру

Тауар қосып көріңіз:
- Мысалы, атауы `Қағаз`, саны `3`, ең аз мөлшері `5` болса, терминалда INFO және WARNING жазбалары көрінеді.
- Қоры шектен жоғары тауар қосқанда INFO жазбасы шығады.
- Атауды бос қалдырсаңыз немесе санды теріс енгізсеңіз, форма қатесі көрсетіліп, WARNING жазылады.

Журналға құпия мәндер немесе тауардың толық сипаттамасы жазылмайды.

## 3. GitHub-қа жіберу

`.env` файлын репозиторийге қоспаңыз. `.gitignore` оны елемейді.

```bash
git init
git add .
git commit -m "Initial warehouse stock tracker"
git branch -M main
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```

## 4. Render арқылы жариялау

1. Render Dashboard ішінде PostgreSQL дерекқорын жасаңыз.
2. Сол аймақта Web Service жасаңыз және GitHub репозиторийін таңдаңыз.
3. Баптаулар:

| Render параметрі | Мәні |
|---|---|
| Runtime | Python 3 |
| Build Command | `bash build.sh` |
| Start Command | `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT` |

4. Environment бөлімінде мына айнымалыларды қосыңыз:

| Айнымалы | Мәні |
|---|---|
| `SECRET_KEY` | Жаңа, кездейсоқ құпия кілт |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-service.onrender.com` (өз доменіңіз) |
| `DATABASE_URL` | PostgreSQL үшін Internal Database URL |

5. Deploy жасаңыз. Build және Runtime Logs бөлімдерінде `collectstatic`, `migrate` және қолданба журналының жазбаларын тексеріңіз.

## 5. Қатені әдейі туғызу және түзету

Жергілікті `.env` ішінде:
```env
DEBUG=False
ALLOWED_HOSTS=localhost
```

Серверді қайта іске қосып, `http://127.0.0.1:8000/` ашыңыз. `400 Bad Request` және терминалда `DisallowedHost` қатесі пайда болады: `127.0.0.1` `ALLOWED_HOSTS` тізіміне енгізілмеген.

Түзету:
```env
ALLOWED_HOSTS=localhost,127.0.0.1
```

Серверді қайта іске қосып, бетті қайта ашыңыз. Бұл сынақты `DEBUG=False` күйінде аяқтаңыз.

## Жоба құрылымы

```text
warehouse_stock_tracker/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── inventory/
│   ├── migrations/0001_initial.py
│   ├── templates/inventory/
│   │   ├── base.html
│   │   └── product_list.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── .env.example
├── build.sh
├── manage.py
└── requirements.txt
```

## Тапсыру алдында

- [ ] Жергілікті жоба іске қосылады.
- [ ] Сынақ тауарын қосқанда INFO жазбасы бар.
- [ ] Қоры аз тауар қосқанда WARNING жазбасы бар.
- [ ] Қате форма жібергенде WARNING жазбасы бар.
- [ ] GitHub репозиторийіне `.env` жүктелмеген.
- [ ] Render URL ашылады.
- [ ] Render Logs скриншоттары түсірілген.
- [ ] `DisallowedHost` қатесі мен түзету нәтижесі көрсетілген.

Ескерту: GitHub репозиторийі мен Render сервисін пайдаланушы өз аккаунтында құрып, Environment айнымалыларын енгізіп, Deploy жасауы керек.
