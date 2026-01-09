from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login

def index(request):
    try:
        context = {'first_name' : request.user.username}
        return render(request, 'index.html', context)
    except AttributeError as e:
        return render(request, 'index.html')

def auth(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
    else:
        return render(request, 'auth.html')

def money(request):
    return render(request, 'money.html')


def reg(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        email = request.POST.get('email')
        # first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        # print(first_name)
        username = email
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return JsonResponse({'status': 'success'})
    else:
      return render(request, 'reg.html')


