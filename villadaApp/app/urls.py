from django.conf.urls import url
from django.urls import include, path
from app import views
from rest_framework import routers

# SET THE NAMESPACE!
router = routers.DefaultRouter()
router.register(r'comunicados', views.ComunicadoViewSet)
router.register(r'alumno', views.AlumnoViewSet)
app_name = 'app'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^redactar/',views.redactar,name='redactar'),
    url(r'^comunicados/',views.comunicados,name='comunicados'),
    path('api', include(router.urls)),
]
