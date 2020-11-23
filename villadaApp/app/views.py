from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from .models import Comunicado, Curso, PadreTutor, Alumno, Formulario, ComunicadoRecibido
from django.template import RequestContext
from django.shortcuts import redirect
from .forms import ComunicadoForm
from django.db.models import Q
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.views import *
from .models import CustomUser as User
from datetime import date

@login_required(login_url="/")
def eliminarComunicados(request, id_comunicado):
    if request.user.groups.filter(name='Padres').exists():
        return redirect('comunicados_padres')
    comunicado = Comunicado.objects.get(id= id_comunicado)
    if request.method == "POST":
        comunicado.delete()
        return redirect('comunicados')
    return render(request, 'delete_comunicado.html',{'comunicado':comunicado})



@login_required(login_url="/")
def redactar(request):
    if request.user.groups.filter(name='Padres').exists():
        return redirect('comunicados_padres')
    if request.method == "POST":
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "redactar.html",{'form':form})
        return redirect('comunicados')
    else:
        today = date.today()
        form = ComunicadoForm(initial={"fecha":today.strftime("%Y-%m-%d")})
    return render(request, "redactar.html",{'form':form})



@login_required(login_url="/")
def comunicados(request):
    if request.user.groups.filter(name='Padres').exists():
        return redirect('comunicados_padres')
    queryset = request.GET.get("buscar")
    comunicados = Comunicado.objects.all().order_by('-fecha')
    if queryset:
        comunicados = comunicados.filter(
        Q(titulo__icontains = queryset)|
        Q(mensaje__icontains = queryset)|
        Q(curso__icontains = queryset)|
        Q(fecha__icontains = queryset)
        ).distinct()

    return render(request ,'comunicados.html', {'comunicados':comunicados})

@login_required(login_url="/")
def display_comunicado(request, id_comunicado):
    comunicado = Comunicado.objects.get(id= id_comunicado)
    return render(request, 'comunicado.html',{'comunicado':comunicado})


@login_required(login_url="/")
def ordenar_por_dir(request, order):
    comunicado = Comunicado.objects.all().order_by('directivo')
    return render(request, 'comunicado.html',{'comunicados':comunicados})


@login_required(login_url="/")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

def user_login(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.groups.filter(name='Padres').exists():
            login(request, user)
            return redirect('comunicados_padres')
        elif user is not None and user.is_superuser:
            login(request, user)
            return redirect('comunicados')
        else:
            return render(request, 'login.html', {'login_message' : 'El Nombre de Usuario o Contraseña son Incorrectos',})
    else:
        return render(request, 'login.html', {})

@login_required(login_url="/")
def formularios(request):
    if request.user.groups.filter(name='Padres').exists():
        return redirect('comunicados_padres')

    queryset = request.GET.get("buscar")
    formularios = Formulario.objects.all().order_by('-fecha')
    if queryset:
        formularios = formularios.filter(
        Q(tipo_form__icontains = queryset)|
        Q(alumno__first_name__icontains = queryset)|
        Q(alumno__last_name__icontains = queryset)|
        Q(fecha__icontains = queryset)
        ).distinct()

    return render(request, 'formularios.html',{'formularios':formularios})

@login_required(login_url="/")
def display_formulario(request, id_formulario):
    formulario = Formulario.objects.get(id= id_formulario)
    return render(request, 'formulario.html',{'formulario':formulario})

class FormView(viewsets.ModelViewSet):
    queryset=Formulario.objects.all()
    serializer_class=FormSerializer

class ComunicadoFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        authorization= request.headers['Authorization']
        array_token = authorization.split()
        token = Token.objects.get(key=array_token[1])
        tutor = PadreTutor.objects.get(user=token.user)
        alumno = Alumno.objects.filter(tutor = tutor.id).values("curso")
        cursos = [a["curso"] for a in alumno]

        return queryset.filter(Q(curso__icontains = alumno)|Q(curso__in = alumno)).order_by('-fecha')

class ComunicadoViewSet(viewsets.ModelViewSet):
    filter_backends = (ComunicadoFilterBackend,)
    queryset = Comunicado.objects.all()
    serializer_class = ComunicadoSer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSer


class UserRecordView(APIView):

    #permission_classes = [IsAdminUser]

    def get(self,  request):

        authorization= request.headers['Authorization']
        array_token = authorization.split()
        token = Token.objects.get(key=array_token[1])
        user = User.objects.filter(username=token.user)
        tutor = PadreTutor.objects.get(user=token.user)
        alumno = Alumno.objects.filter(tutor=tutor.id)
        serializer_tutor = UserSerializer(user, many=True)
        serializer_hijo = AlumnooSer(alumno, many=True)
        alumno_padre = [(serializer_tutor.data)[0], (serializer_hijo.data)[0]]
        return Response(alumno_padre)

    def post(self, request):
        print(request.data)
        serializer = Serializer(data=request.data)
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

class ComunicadoRecibidoView(APIView):

        def post(self, request):
            recibido = request.data['recibido']
            comunicado = request.data['comunicado']

            authorization= request.headers['Authorization']
            array_token = authorization.split()
            token = Token.objects.get(key=array_token[1])
            tutor = PadreTutor.objects.get(user=token.user)

            comunicado_recibido = ComunicadoRecibido.objects.filter(padre_tutor=tutor.id, comunicado=comunicado).update(recibido=recibido)
            
            return Response(
                status=status.HTTP_201_CREATED
            )
