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
git clone https://github.com/
```

Переходим в директорию meetup/server в проекте, там нужно создать .env файл с вот такими переменными

```dotenv
TZ="% Ваш часовой пояс например Europe/Moscow %"
WEBHOOK_API_TOKEN="% Сгеннерируйте токен сами (uuidgen, openssl) %"
```

Переходим в директорию meetup/client/src в файл consts.ts в нем надо изменить константу `TZ` на свой часовой пояс

```typescript
export const TZ = "Eroupe/Moscow";
```

Дальше переходим к запуску проекта, нужно перейти в директорию проекта где находится файл `docker-compose.yml`

```bash
cd meetup/
docker-compose up --build
```

Ждем окончательного запуска и можно пользоваться

---
### Список адресов проекта

`http://localhost:3000/` - React Client

`http://localhost:8000` - Server API

`http://localhost:8001` - Telegram Bot webhook handler  

---

### Стек технологий

#### Frontend
`TypeScript`, `React`, `Redux`, `React-Router-DOM`, `React-Icons`, `moment`.

В `React` я использовал подход на классовых компонентах, предпочел его функциональному подходу
, но знаю я и использую (иногда) функциональный подход.

#### Backend
`Python`, `FastAPI`, `Celery`, `TortoiseORM`, `asyncpg`, `aiogram`

...