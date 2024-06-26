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
    path('posteoCreacion/', PosteoCreacion.as_view(), name='nuevo_posteo'),
    path('posteos/', views.obtener_posteos, name='obtener_posteos'),
    path('dar_like/', dar_like, name='dar_like'),
    path('dar_dislike/', dar_dislike, name='dar_dislike'),
    path('posteoEstadisticas/', posteo_estadisticas, name='posteo_estadisticas'),
    path('misInteracciones/', user_interactions, name='user_interactions'),
    path('eliminarPosteo/<int:posteo_id>/', eliminar_posteo, name='eliminar_posteo'),
    path('listaPosteos/', lista_posteos_delete, name='lista_posteos'),
    path('acercaDeMi/', views.acerca_de_mi, name='acerca_de_mi'),
]
