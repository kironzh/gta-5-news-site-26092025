from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('reg/', views.reg, name='reg'),
    path('money', views.money, name='money')
]
