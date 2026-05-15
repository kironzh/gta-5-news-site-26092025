## Необходимые инструменты и запуск

Клонируйте репозиторий:

```shell
git clone https://github.com/kironzh/gta-5-news-site-26092025
```
И затем запустите:

```shell
py manage.py runserver
```

## По работе с электронной почтой
Вы должны добавить файл *personal_info.py* в папку *gta_5_news_site/gta_5_news_site_app*, где должен располагаться следующий код:

```python
MY_EMAIL_HOST_USER = 'почтовый_адрес'
MY_EMAIL_HOST_PASSWORD = 'пароль'
```

Если вы не хотите работать с почтовым сервером, вы можете использовать *django.core.mail.backends.console.EmailBackend* вместо SMTP-сервера в settings.py. Просто замените значение в константе EMAIL_BACKEND на *'django.core.mail.backends.console.EmailBackend'*.

## Чтобы сделать миграцию файлов

```shell
py manage.py makemigrations
```
А затем:

```shell
py manage.py migrate
```