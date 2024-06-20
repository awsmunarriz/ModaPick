from django.views.generic import UpdateView
from django.views.generic.edit import CreateView, UpdateView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Count, Q, F, ExpressionWrapper, IntegerField
from django.urls import reverse_lazy
from .forms import FormularioCambioPassword, FormularioEdicion, FormularioRegistroUsuario
from .forms import FormularioNuevoPosteo

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Favoritos

import json


def home(request):
    return render(request, 'home.html')

class LoginPagina(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'passwordExitoso.html', {})

def chequeo(request):
    return render(request, 'check.html', {})


# NUEVO POSTEO
class PosteoCreacion(LoginRequiredMixin, CreateView):
    model = Post
    form_class = FormularioNuevoPosteo
    success_url = reverse_lazy('home')
    template_name = 'posteoCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PosteoCreacion, self).form_valid(form)

# OBTENER POSTEOS
def obtener_posteos(request):
    posteos = Post.objects.all()
    user_authenticated = request.user.is_authenticated
    data = {
        'authenticated': user_authenticated,
        'posteos': [
            {
                'id': posteo.id,
                'title': posteo.title,
                'description': posteo.description,
                'created_at': posteo.created_at,
                'imagen': posteo.imagen.url if posteo.imagen else '',
            }
            for posteo in posteos
        ]
    }
    return JsonResponse(data, safe=False)

# DAR LIKE A POSTEO
def dar_like(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if 'posteo_id' not in data:
                response_data = {"status": "error", "message": "Missing 'posteo_id' parameter"}
                return JsonResponse(response_data, status=400)  # 400 Bad Request
            posteo_id = data['posteo_id']
            posteo = Post.objects.get(id=posteo_id)
            Favoritos.objects.filter(user=request.user, posteo=posteo).delete()  # Eliminar cualquier interacción previa
            Favoritos.objects.create(user=request.user, posteo=posteo, interaction=Favoritos.LIKE)
            response_data = {"status": "success", "message": "Like added"}
        except json.JSONDecodeError:
            response_data = {"status": "error", "message": "Invalid JSON"}
    else:
        response_data = {"status": "error", "message": "Invalid request method"}
    return JsonResponse(response_data)


# DAR DISLIKE A POSTEO
def dar_dislike(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if 'posteo_id' not in data:
                response_data = {"status": "error", "message": "Missing 'posteo_id' parameter"}
                return JsonResponse(response_data, status=400)  # 400 Bad Request
            posteo_id = data['posteo_id']
            posteo = Post.objects.get(id=posteo_id)
            Favoritos.objects.filter(user=request.user, posteo=posteo).delete()  # Eliminar cualquier interacción previa
            Favoritos.objects.create(user=request.user, posteo=posteo, interaction=Favoritos.DISLIKE)
            response_data = {"status": "success", "message": "Dislike added"}
        except json.JSONDecodeError:
            response_data = {"status": "error", "message": "Invalid JSON"}
    else:
        response_data = {"status": "error", "message": "Invalid request method"}
    return JsonResponse(response_data)


# Obtener estadísticas de likes y dislikes (staff)
@staff_member_required
def posteo_estadisticas(request):
    # Obtener los posteos con sus estadísticas de likes y dislikes y calcular la puntuación
    posteos = Post.objects.annotate(
        likes=Count('favoritos', filter=Q(favoritos__interaction=Favoritos.LIKE)),
        dislikes=Count('favoritos', filter=Q(favoritos__interaction=Favoritos.DISLIKE)),
        puntuacion=ExpressionWrapper(
            Count('favoritos', filter=Q(favoritos__interaction=Favoritos.LIKE)) - Count('favoritos', filter=Q(favoritos__interaction=Favoritos.DISLIKE)),
            output_field=IntegerField()
        )
    )
    context = {
        'posteos': posteos
    }
    return render(request, 'posteo_estadisticas.html', context)


# Obtener los Likes y Dislikes (usuario autenticado)
@login_required
def user_interactions(request):
    favoritos = Favoritos.objects.filter(user=request.user).select_related('posteo')

    context = {
        'favoritos': favoritos
    }
    return render(request, 'user_interactions.html', context)
