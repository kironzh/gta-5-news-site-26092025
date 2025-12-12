from django.shortcuts import render

def index(request):
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

