from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from .models import News

def index(request):
    try:
        context = {'first_name' : request.user.username}
        return render(request, 'index.html', context)
    except AttributeError as e:
        return render(request, 'index.html')

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'status' : 'success'})
        else:
            return JsonResponse({ 'status' : 'error'})
    else:
        return render(request, 'auth.html')

def money(request):
    return render(request, 'money.html')


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
        return JsonResponse({'status': 'success'})
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


