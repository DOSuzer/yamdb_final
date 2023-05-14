![example workflow](https://github.com/dosuzer/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# YaMDb API

Server IP:  158.160.30.120

### Описание
YaMDb собирает отзывы (Reviews) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Categories) может быть расширен Администратором. Произведению может быть присвоен жанр (Genre) из списка предустановленных (например: «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только Администратор. Пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку (Score) в диапазоне от 1 до 10; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (Raiting). На одно произведение пользователь может оставить только один отзыв. Пользователи могут оставлять комментарии к отзывам. Для авторизации пользователей используется код подтверждения высылаемый на email. Для аутентификации пользователей используются JWT-токены.

Проект развернут в docker-контейнере состоящем из трех отдельных контейнеров:
- web - веб сервер django <-> gunicorn
- db - база данных postgres
- nginx - HTTP-сервер nginx

Таким образом можно легко запустить проект на любом компьютере или сервере следуя дальнейшим инструкциям. 

### Технологии:
Python, Django, DRF, Simple JWT, Docker, Gunicorn, NGINX, PostgreSQL, CI-CD

### Шаблон .env:
В папке infra создайте файл .env
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=password # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

### Как запустить проект:

1.Перейти в папку с файлом docker-compose.yaml
```
cd ~/infra_sp2/infra/
```
2.Запустить сборку
```
docker-compose up
```
3.Выполнить миграции
```
docker-compose exec web python manage.py migrate
```
4.Создать суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
5.Собрать статику
```
docker-compose exec web python manage.py collectstatic --no-input
```

### Заполнение БД:
1.Из sql файла:
```
docker cp ./localfile.sql infra-db-1:/app/file.sql
docker exec -u POSTGRES_USER infra-db-1 psql DB_NAME POSTGRES_USER -f /app/file.sql
```
2.Из json файла:
```
docker cp ./localfile.json infra-web-1:/app/file.json
docker-compose exec web python3 manage.py shell
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
docker-compose exec web python3 loaddata file.json
```

### Развернуть проект на удаленном сервере:

Для запуска проекта на удаленном сервере необходимо:

- скопировать на сервер файл docker-compose.yaml, файл конфигурации nginx default.conf (команды выполнять находясь в директории с файлом):
```
scp docker-compose.yaml username@host:home/username/docker-compose.yaml

scp default.conf username@host:home/username/nginx/default.conf
```

- В разделе Secrets > Actions репозитория создать переменные окружения:
```
DOCKER_PASSWORD         # пароль от Docker Hub
DOCKER_USERNAME         # логин Docker Hub
HOST                    # публичный IP сервера
USER                    # имя пользователя на сервере
PASSPHRASE              # если ssh-ключ защищен паролем
SSH_KEY                 # приватный ssh-ключ
TELEGRAM_TO             # ID телеграм-аккаунта для сообщения
TELEGRAM_TOKEN          # токен бота

DB_ENGINE               # django.db.backends.postgresql
DB_NAME                 # postgres
POSTGRES_USER           # postgres
POSTGRES_PASSWORD       # свой пароль
DB_HOST                 # db
DB_PORT                 # 5432
```

### После каждого обновления репозитория будет происходить:

1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest
2. Сборка и доставка докер-образа для контейнера web на Docker Hub
3. Разворачивание проекта на удаленном сервере
4. Отправка сообщения в Telegram в случае успеха


### Примеры запросов к API:

- Получение списка всех произведений: доступно без токена.

*Запрос:*

```
GET http://localhost/api/v1/titles/
```

*Пример ответа:*

```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]
```

- Добавление нового отзыва к произведению: доступно аутентифицированным пользователям.

*Запрос:*

```
POST http://localhost/api/v1/titles/{title_id}/reviews/
```

*Содержимое запроса:*

```
{
  "text": "string",
  "score": 1
}
```

*Пример ответа:*

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 10,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

- Добавление комментария к отзыву: доступно аутентифицированным пользователям.

*Запрос:*

```
POST http://localhost/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

*Содержимое запроса:*

```
{
  "text": "string"
}
```

*Пример ответа:*

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```

- Удаление пользователя по имени пользователя (username): доступно Администратору.

*Запрос:*

```
DELETE http://localhost/api/v1/users/{username}/
```
