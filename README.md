# MeetUP

Веб-приложение позволяющие создавать встречи между зарегистрированными
в системе людьми.

---
### Зависимости
Для корректного развертывания приложения вам надо установить
`docker`, `docker-compose`.

---
### Установка зависимостей

Сначала обновите текущие пакеты

```bash
sudo apt update
```

После установите необходимые пакеты, которые позволят `apt`
устанавливать пакеты через HTTPS

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
    
Добавьте GPG ключ для официального репозитория `Docker`

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Добавьте репозиторий `Docker`

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```

Обновите пакеты через 
```bash
sudo apt update
```

Теперь можете установить сам `Docker`

```bash
sudo apt install docker-ce
```

Дальше проверьте что `Docker` установился правильно

```bash
sudo docker run hello-world
```
---
**Теперь установим `docker-compose`**

Загрузите последнюю версию `docker-compose` с помощью следующей команды

```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Выдаем права для выполнения загружаемого файла

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

Создаем ссылку на `docker-compose`, чтобы было удобно его запускать (необязательно, но необходимо)

```bash
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

Проверяем что `docker-compose` установился правильно и идем дальше

```bash
docker-compose --version
```
---
### Установка MeetUP

Дальше будет описаны шаги установки приложения на ваш ПК или сервер с последующим запуском

Клонируем репозиторий

```bash
git clone git@github.com:FatJun/meetup.git
```

Переходим в директорию `meetup/server` в проекте, там нужно создать `.env` файл с вот такими переменными

```dotenv
TZ=Ваш_часовой_пояс_например_Europe/Moscow
WEBHOOK_API_TOKEN=Сгеннерируйте_токен_сами_(uuidgen,_openssl)

POSTGRES_USER=YOUR_USERNAME
POSTGRES_PASSWORD=YOUR_PASSWORD
POSTGRES_DB=YOUR_POSTGRES_DB_NAME
```

Переходим в директорию `meetup/client/src` в файл `consts.ts` в нем надо изменить константу `TZ` на свой часовой пояс

```typescript
export const TZ = "Eroupe/Moscow";
```

Настройка `docker-compose.yml`, он должен лежать в корневой папке 

```.
└── meetup
    ├── docker-compose.yml
    ├── .gitignore
    ├── .babelrc
    ├── README.md
    └── meetup
        ├── client
        ├── server
        └── ...
```
`docker-compose.yml`
```yaml
version: '3'

services:
  app:
    build:
      dockerfile: ./app.Dockerfile
      context: ./meetup/server/
    command: poetry run python3 -m app.main
    ports:
      - "8000:8000"
    depends_on:
      - db
      
  telegram-bot:
    build:
      dockerfile: ./telegram_bot.Dockerfile
      context: ./meetup/server/
    command: poetry run python3 -m telegram_bot.main
    environment:
      - TELEGRAM_BOT_API_TOKEN=YOUR_TELEGRAM_TOKEN
    ports:
      - "8001:8001"
    depends_on:
      - db
      - celery-worker

  celery-worker:
    build:
      dockerfile: ./celery_worker.Dockerfile
      context: ./meetup/server/
    command: poetry run celery -A scheduler worker --loglevel=info
    depends_on:
      - redis
      
  client:
    build: ./meetup/client
    command: npm start
    ports:
      - "3000:3000"
    depends_on:
      - app
      
  redis:
    image: redis:latest
    ports:
      - "6379:6379"
      
  db:
    image: postgres
    environment:
      - POSTGRES_USER=YOUR_DB_USERNAME
      - POSTGRES_PASSWORD=YOUR_DB_PASSWORD
      - POSTGRES_DB=YOUR_DB_NAME
    ports:
      - "5432:5432"
```

Дальше переходим к запуску проекта, нужно перейти в директорию проекта где находится файл `docker-compose.yml`

```bash
cd meetup/
docker-compose up --build
```

Ждем окончательного запуска и можно пользоваться

---
### Список адресов проекта

`http://localhost:3000` - React Client

`http://localhost:8000` - Server API

`http://localhost:8001` - Telegram Bot webhook handler  

---

### Стек технологий

#### Frontend
`TypeScript`, `React`, `Redux`, `React-Router-DOM`, `React-Icons`, `moment`.

В `React` я использовал подход на классовых компонентах, предпочел его функциональному подходу,
но также я знаю и использую (иногда) функциональный подход.

#### Backend
`Python`, `FastAPI`, `Celery`, `TortoiseORM`, `asyncpg`, `aiogram`

...