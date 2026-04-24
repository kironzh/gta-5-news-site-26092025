from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from .models import News
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import random

def index(request):
    print(request.user.username)
    # try:
    #     context = {'first_name' : request.user.username}
    #     return render(request, 'index.html', context)
    # except AttributeError as e:
    #     return render(request, 'index.html')
    context = {'first_name' : request.user.username}
    return render(request, 'index.html', context)

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print(user, email, password)
        if user:
            login(request, user)
            return redirect ('index')
        else:
            return JsonResponse({ 'status' : 'error'})
    else:
        return render(request, 'auth.html')

def money(request):
    return render(request, 'money.html')

def media(request):
    return render(request, 'media.html')

def food(request):
    return render(request, 'food.html')

def travel(request):
    return render(request, 'travel.html')

def fashion(request):
    return render(request, 'fashion.html')

def sponsors(request):
    return render(request, 'sponsors.html')


def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        print(first_name)
        username = email
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        #return JsonResponse({'status': 'success'})
        return redirect('index')
    else:
      return render(request, 'reg.html')
    
def logout_view(request):
    logout(request)
    return redirect('index')

def news_template(request, id):
    news = News.objects.get(id = id) 
    context = { 
        'news_title' : news.news_title,
        'image' : news.image,
        'news_text' : news.news_text,
        'pub_date' : news.pub_date,
        'news_source' : news.news_source
    }
    return render(request, 'news_template.html', context)

def news_list(request, news_type):
    news_type_name = ''

    if news_type == 'all':
        news = News.objects.all()
        news_type_name = 'Все новости'
    else:
        news = News.objects.filter(news_type = news_type)
        news_types = News.types

        for nt in news_types:
            if nt[0] == news_type:
                news_type_name = nt[1]
                break
    context = {
        'news_list' : news,
        'news_type' : news_type_name
    }
    return render(request, 'news_list.html', context)

def account(request):
    print(request.user.id)
    context = {
        'username' : request.user.username,
        'email' : request.user.email,
        'first_name' : request.user.first_name,
        'password' : request.user.password,
    }
    return render(request, 'account.html', context)

def email(request):
    if request.method == 'POST' and request.POST.get('email'):
        
        try:
            email = request.POST.get('email')
            validate_email(email)
            print('Получилось взять имейл: ', email)
        except ValidationError:
            return JsonResponse({'status': 'error', 'message' : 'Неправильно ввёден адрес почты'}, status=400)

        send_mail(
            "Проверка из Django",
            "Привет из Django!",
            'kironzh@yandex.ru',
            [str(email)],
            fail_silently=False,
        )


        return JsonResponse({'status': 'success', 'message' : 'Отправлено'})
    return JsonResponse({'status' : 'error', 'message' : 'Метод не разрешён. Только POST.'}, status=405)

def generate_code(request):
    print(random.randint(100000,999999))
    return render(request, 'generate_code.html')





