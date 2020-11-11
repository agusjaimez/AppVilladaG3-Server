from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from .models import Comunicado, Curso, PadreTutor, Alumno
from django.template import RequestContext
from django.shortcuts import redirect
from .forms import ComunicadoForm
from django.db.models import Q
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from rest_framework.authtoken.views import *


def index(request):
    return render(request,'index.html')

@login_required
def eliminarComunicados(request, id_comunicado):
    comunicado = Comunicado.objects.get(id= id_comunicado)
    if request.method == "POST":
        comunicado.delete()
        return redirect('comunicados')
    return render(request, 'delete_comunicado.html',{'comunicado':comunicado})


#Todavia no usamos esta vista, pero la dejo por si las dudas despues la usamos...
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
    queryset = request.GET.get("buscar")
    comunicados = Comunicado.objects.all().order_by('fecha')
    if queryset:
        comunicados = Comunicado.objects.filter(
        Q(titulo__icontains = queryset)|
        Q(mensaje__icontains = queryset)
        ).distinct()

    return render(request ,'comunicados.html', {'comunicados':comunicados})

@login_required
def display_comunicado(request, id_comunicado):
    comunicado = Comunicado.objects.get(id= id_comunicado)
    return render(request, 'comunicado.html',{'comunicado':comunicado})

@login_required
def ordenar_por_dir(request, order):
    comunicado = Comunicado.objects.all().order_by('directivo')
    return render(request, 'comunicado.html',{'comunicados':comunicados})

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
        if user is not None and user.groups.filter(name='Padres').exists():
            login(request, user)
            return redirect('hola_padres')
        elif user is not None:
            login(request, user)
            return redirect('comunicados')
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


""" def curso_tipo(response):
    curso = response.get["curso"]
    return ComunicadoCurso.objects.all().filter(cursos_name = curso).values_list('id', flat=True) """

class ComunicadoViewSet(viewsets.ModelViewSet):
    queryset = Comunicado.objects.all()
    serializer_class = ComunicadoSer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSer


class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        #print((super(CustomObtainAuthToken, self).post(request, *args, **kwargs)).data['token'])
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

# class CustomObtainAuthToken(ObtainAuthToken):
#     def get(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['token'])
#
#         return Response({'token': token.key, 'user': token.username})
