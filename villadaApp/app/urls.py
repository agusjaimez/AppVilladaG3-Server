from django.conf.urls import url
from app import views
# SET THE NAMESPACE!
app_name = 'app'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^redactar/',views.redactar,name='redactar'),
    url(r'^comunicados/',views.comunicados,name='comunicados'),
]
