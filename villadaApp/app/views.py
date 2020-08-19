from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,'index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email=="grupo3@gmail.com"and password=="grupo3":
            return render(request, 'comunicados.html', {})
        else:
            return HttpResponse("CASI bro")
    else:
        return render(request, 'login.html', {})
def redactar(request):
    return render(request ,'redactar.html',{})
def comunicados(request):
    return render(request ,'comunicados.html',{})
    