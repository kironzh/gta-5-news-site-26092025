from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('reg/', views.reg, name='reg'),
    path('money', views.money, name='money'),
    path('logout/', views.logout_view, name='logout'),
    path('news/<int:id>', views.news_template, name='news')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
