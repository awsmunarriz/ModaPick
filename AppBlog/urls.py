from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from AppBlog.views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/', views.password_exitoso, name='password_exitoso'),
    path('check/', views.chequeo, name='chequeo'),
    path('posteoCreacion/', PosteoCreacion.as_view(), name='nuevo'),
    path('posteos/', views.obtener_posteos, name='obtener_posteos'),
    path('agregar_a_favoritos/', agregar_a_favoritos, name='agregar_a_favoritos'),
]
