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
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^usuario_padres/',views_padres.usuario_padres,name='usuario_padres'),
    url(r'^comunicados_padres/',views_padres.comunicados_padres,name='comunicados_padres'),
    ##-------------------------------------------------------
    path('api', include(router.urls)),
]
