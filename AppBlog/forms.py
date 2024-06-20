from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Post

class FormularioRegistroUsuario(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name',
                  'last_name', 'password1', 'password2')


class FormularioEdicion(UserChangeForm):
    password = None
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')


class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label=("Confirmar Nuevo Password"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


# class FormularioNuevoPosteo(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'description', 'imagen')

#         widgets = {
#             'title' : forms.TextInput(attrs={'class': 'form-control'}),
#             'description' : forms.TextInput(attrs={'class': 'form-control'}),
#         }

class FormularioNuevoPosteo(forms.ModelForm):
    title = forms.CharField(label=("Titulo"),
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label=("Descripcion"),
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ('title', 'description', 'imagen')
