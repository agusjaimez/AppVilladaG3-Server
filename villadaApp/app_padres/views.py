from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from app.models import Comunicado, Curso, PadreTutor, Alumno
from django.template import RequestContext
from django.shortcuts import redirect
from app.forms import ComunicadoForm
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
#from django.contrib.auth.models import User
from app.models import CustomUser as User


@login_required(login_url="/")
def comunicados_padres(request):
    if request.user.groups.filter(name='Padres').exists() == False:
        return render(request, 'login.html', {})

    queryset = request.GET.get("buscar")
    padre = PadreTutor.objects.filter(user=request.user.id)[0]
    alumno = Alumno.objects.filter(tutor = padre.id).values("curso")
    cursos = [a["curso"] for a in alumno]
    comunicados = Comunicado.objects.filter(Q(curso__icontains = alumno)|Q(curso__in = alumno)).order_by('fecha')
    if queryset:
        comunicados = comunicados.filter(
        Q(titulo__icontains = queryset)|
        Q(mensaje__icontains = queryset)|
        Q(fecha__icontains = queryset)
        ).distinct()
    return render(request ,'comunicados_padres.html', {'comunicados':comunicados})

@login_required(login_url="/")
def display_comunicado_padres(request, id_comunicado):
    if request.user.groups.filter(name='Padres').exists() == False:
        return render(request, 'login.html', {})
    comunicado = Comunicado.objects.get(id= id_comunicado)
    return render(request, 'comunicado_padres.html',{'comunicado':comunicado})

@login_required(login_url="/")
def ordenar_por_dir_padres(request, order):
    comunicado = Comunicado.objects.all().order_by('directivo')
    return render(request, 'comunicado_padres.html',{'comunicados':comunicados})

@login_required(login_url="/")
def usuario_padres(request):
    if request.user.groups.filter(name='Padres').exists() == False:
        return render(request, 'login.html', {})
    tutor = PadreTutor.objects.filter(user=request.user.id)[0]
    alumno = Alumno.objects.filter(tutor = tutor.id)
    return render(request, 'usuario_padres.html', {"tutor":tutor,"alumnos":alumno})
