from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate


def index(request):
    return render(request,'index.html')

def redactar(request): 
    return render(request ,'redactar.html',{})

def comunicados(request):
    return render(request ,'comunicados.html',{})

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request, 'comunicados.html', {})
        else:
            return HttpResponse("CASI bro")
    else:
        return render(request, 'login.html', {})
