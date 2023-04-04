![example workflow](https://github.com/dosuzer/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Server IP:  158.160.30.120

### Описание
Данный проект предоставляет доступ к сервису YaMDb посредством API. 
Основные возможности:
- просматривать раличные произведения
- писать отзывы на произведения
- ставить оценку произведениям
- комментировать отзывы других пользователей

Проект развернут в docker-контейнере состоящем из трех отдельных контейнеров:
- web - веб сервер django <-> gunicorn
- db - база данных postgres
- nginx - HTTP-сервер nginx

Таким образом можно легко запустить проект на любом компьютере или сервере следуя дальнейшим инструкциям. 

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

### Регистрация и утентификация:
Вам доступны такие эндпойнты:
- api/v1/auth/signup/ - регистрация в сервисе yamdb
- api/v1/auth/token/ - получение токена авторизации в сервисе yamdb
- api/v1/users/ - просмотр, создание и редактирование пользователей (для администратора)
- api/v1/users/me/ - редактирование данных своего профиля

Пример регистрации (POST запрос к api/v1/auth/signup/):
```
{
    "username":"User1",
    "email":"user1@ya.ru"
}
```
Пример получения токена (POST запрос к api/v1/auth/token/):
```
{
    "username":"User1",
    "confirmation_code":"89cbba4f-2c6b-4650-8f78-347055c193fd"
}
```
Пример добавления пользователя (POST запрос к api/v1/users/):
```
{
    "username":"User2",
    "email":"user2@ya.ru",
    "first_name":"Вася",
    "last_name":"Пупкин"
}
```
Пример редактирования данных своего профиля (POST запрос к api/v1/users/me/):
```
{
    "first_name":"Иван",
    "last_name":"Иванов"
}
```
