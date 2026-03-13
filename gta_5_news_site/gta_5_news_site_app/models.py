from django.db import models
import os
from django.conf import settings

def news_text_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "news-text")

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "images")




class News(models.Model):
    types = (
        ('Нов', 'Новость'),
        ('Стат', 'Статья')
    )
    news_title = models.CharField(max_length = 100) #заголовок
    news_text = models.TextField() #текст новости
    image = models.ImageField() #изображение
    pub_date = models.DateField(max_length = 20) #дата публикации
    news_source = models.CharField(max_length = 20, default='Weazel News') #источник новости
    news_type = models.CharField(max_length = 20, choices=types)
    def __str__(self):
        return f'{self.id}. {self.news_title}'
