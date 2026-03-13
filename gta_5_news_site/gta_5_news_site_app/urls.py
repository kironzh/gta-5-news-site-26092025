from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('reg/', views.reg, name='reg'),
    path('money/', views.money, name='money'),
    path('media/', views.media, name='media'),
    path('food/', views.food, name='food'),
    path('travel/', views.travel, name='travel'),
    path('fashion/', views.fashion, name='fashion'),
    path('logout/', views.logout_view, name='logout'),
    path('news/<int:id>', views.news_template, name='news'),
    path('news/', views.news_list, name='news_list')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
