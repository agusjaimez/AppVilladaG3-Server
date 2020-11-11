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
from django.contrib.auth.models import User



def hola_padres(request):
    if request.method == "POST":
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('comunicados')
    else:
        form = ComunicadoForm()
    return render(request, "hola_padres.html")


@login_required
def comunicados_padres(request):
    queryset = request.GET.get("buscar")
    padre = PadreTutor.objects.filter(user=request.user.id)[0]
    alumno = Alumno.objects.filter(tutor = padre.id).values("curso")
    cursos = [a["curso"] for a in alumno]
    comunicados = Comunicado.objects.filter(Q(curso__in = alumno)).order_by('fecha')
    if queryset:
        comunicados = Comunicado.objects.filter(
        Q(curso__in = alumno),
        Q(titulo__icontains = queryset)|
        Q(mensaje__icontains = queryset)
        ).distinct()

    return render(request ,'comunicados_padres.html', {'comunicados':comunicados})

@login_required
def display_comunicado_padres(request, id_comunicado):
    comunicado = Comunicado.objects.get(id= id_comunicado)
    return render(request, 'comunicado_padres.html',{'comunicado':comunicado})

@login_required
def ordenar_por_dir_padres(request, order):
    comunicado = Comunicado.objects.all().order_by('directivo')
    return render(request, 'comunicado_padres.html',{'comunicados':comunicados})

@login_required
def usuario_padres(request):

    tutor = PadreTutor.objects.filter(user=request.user.id)[0]
    alumno = Alumno.objects.filter(tutor = tutor.id)


    return render(request, 'usuario_padres.html', {"tutor":tutor,"alumnos":alumno})
    
    
    
    
    
    
    
    
    
    
