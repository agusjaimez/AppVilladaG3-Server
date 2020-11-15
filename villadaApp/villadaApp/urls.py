"""villadaApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from app import views,urls
from app_padres import views as views_padres
from rest_framework.authtoken import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^app/',include('app.urls')),
    url(r'^$',views.user_login,name='user_login'),
    url(r'^comunicados/',views.comunicados,name='comunicados'),
    url(r'^usuario_padres/',views_padres.usuario_padres,name='usuario_padres'),
    url(r'^comunicados_padres/',views_padres.comunicados_padres,name='comunicados_padres'),
    url(r'^comunicados/',views.ordenar_por_dir,name='ordenar_por_dir'),
    url(r'^comunicados_padres/',views_padres.ordenar_por_dir_padres,name='ordenar_por_dir'),
    url(r'^comunicado/(?P<id_comunicado>\d+)/$',views.display_comunicado,name='display_comunicado'),
    url(r'^comunicado_padres/(?P<id_comunicado>\d+)/$',views_padres.display_comunicado_padres,name='display_comunicado_padres'),
    url(r'^delete/(?P<id_comunicado>\d+)/$',views.eliminarComunicados,name='delete_comunicados'),
    url(r'^redactar/',views.redactar,name='redactar'),
    url(r'^logout/',views.user_logout,name='user_logout'),
    path('api-token-auth/', auth_view.obtain_auth_token, name='api-token-auth'),
    path('editar_usuario/', views_padres.editar_usuario, name='editar_usuario'),

]
