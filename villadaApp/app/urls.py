from django.conf.urls import url
from django.urls import include, path
from app import views
from app_padres import views as views_padres
from rest_framework import routers
# SET THE NAMESPACE!
router = routers.DefaultRouter()
router.register(r'comunicados', views.ComunicadoViewSet)
router.register(r'comunicados_padres', views.ComunicadoViewSet)
router.register(r'alumno', views.AlumnoViewSet)
app_name = 'app'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^redactar/',views.redactar,name='redactar'),
    url(r'^comunicados/',views.comunicados,name='comunicados'),
    url(r'^hola_padres/',views_padres.hola_padres,name='hola_padres'),
    url(r'^usuario_padres/',views_padres.usuario_padres,name='usuario_padres'),
    url(r'^comunicados_padres/',views_padres.comunicados_padres,name='comunicados_padres'),
    path('api', include(router.urls)),
    path('user/', views.UserRecordView.as_view(), name='users'),
]
