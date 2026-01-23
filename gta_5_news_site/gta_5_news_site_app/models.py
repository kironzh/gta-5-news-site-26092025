from django.db import models
import os
from django.conf import settings

def news_text_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "news-text")

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "images")


class News(models.Model):
    news_title = models.CharField(max_length = 100) #заголовок
    news_text = models.FilePathField(path = news_text_path) #текст новости
    image = models.FilePathField(path = images_path) #изображение
    pub_date = models.DateField(max_length = 20) #дата публикации
    news_source = models.CharField(max_length = 20) #источник новости
