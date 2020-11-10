from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
##-------------------------------------------------------
from app_padres import views as views_padres
##-------------------------------------------------------
# SET THE NAMESPACE!
router = routers.DefaultRouter()
app_name = 'app_padres'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    ##-------------------------------------------------------
    url(r'^hola_padres/',views_padres.hola_padres,name='hola_padres'),
    url(r'^usuario_padres/',views_padres.usuario_padres,name='usuario_padres'),
    url(r'^comunicados_padres/',views_padres.comunicados_padres,name='comunicados_padres'),
    ##-------------------------------------------------------
    path('api', include(router.urls)),
]
