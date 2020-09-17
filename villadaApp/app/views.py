from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from .models import Comunicado, Curso
from django.template import RequestContext
from django.shortcuts import redirect
from .forms import ComunicadoForm


def index(request):
    return render(request,'index.html')

@login_required
def eliminarComunicados(request, id_comunicado):
    comunicado = Comunicado.objects.get(id= id_comunicado)
    if request.method == "POST":
        comunicado.delete()
        return redirect('comunicados')
    return render(request, 'delete_comunicado.html',{'comunicado':comunicado})


#Todavia no usamos esta vista, pero la dejo por si las dudas despues si...
@login_required
def editarComunicados(request, id_comunicado):
    comunicado = Comunicado.objects.get(id= id_comunicado)
    if request.method == "GET":
        form = ComunicadoForm(instance=comunicado)
    else:
        form = ComunicadoForm(request.POST, instance=comunicado)
        if form.is_valid():
            form.save
        return redirect('comunicados')
    return render(request, "redactar.html")

@login_required
def redactar(request):
    if request.method == "POST":
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('comunicados')
    else:
        form = ComunicadoForm()
    return render(request, "redactar.html",{'form':form})

@login_required
def comunicados(request):
    comunicados = Comunicado.objects.all().order_by('fecha')
    return render(request ,'comunicados.html', {'comunicados':comunicados})



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
            login(request, user)
            return redirect('comunicados')

        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})
""" def curso_tipo(response):
    curso = response.get["curso"]
    return ComunicadoCurso.objects.all().filter(cursos_name = curso).values_list('id', flat=True) """
