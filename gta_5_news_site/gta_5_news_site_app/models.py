from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import secrets

def news_text_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "news-text")

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "images")

class Vasya(models.Model):
    test = 'hello'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)

class News(models.Model):
    types = (
        ('hot_news', 'Горячие новости'),
        ('top_of_the_week', 'Топ недели'),
        ('recomendations', 'Рекомендуем'),
        ('news_of_the_day', 'Новость дня'),
        ('media', 'СМИ и развлечения'),
        ('food', 'Еда и напитки'),
        ('money', 'Деньги и услуги'),
        ('travel', 'Путешествия и транспорт'),
        ('fashion', 'Мода и здоровье'),
     )
    
    news_title = models.CharField(max_length = 200) #заголовок
    news_text = models.TextField() #текст новости
    image = models.ImageField() #изображение
    pub_date = models.DateField(max_length = 20) #дата публикации
    news_source = models.CharField(max_length = 20, default='Weazel News') #источник новости
    news_type = models.CharField(max_length = 20, choices=types)
    def __str__(self):
        return f'{self.id}. {self.news_title}'
    
class EmailCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

# class ObjectDoesNotExist(models.Model):
#     types = (
#      )
    
#     def is_expired(self):
#         return timezone.now() > self.created_at + timedelta(minutes=30)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-date']

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now, null=True)
    moderation = models.BooleanField(default=False)

    def __str__(self):
        return self.text