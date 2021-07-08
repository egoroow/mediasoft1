from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ('actor_id', 'actor_name', 'actor_surname', 'actor_patronymic')


class ProducerForm(ModelForm):
    class Meta:
        model = Producer
        fields = ('producer_id', 'producer_name', 'producer_surname', 'producer_patronymic')


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ('genre_id', 'genre_title')


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_id', 'movie_title', 'movie_genre', 'movie_producer', 'movie_actor', 'movie_description', 'movie_trailer', 'movie_mark', 'movie_img')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь {username} не найден')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Введен неверный пароль')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Данный email занят')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с именем {username} уже зарегистрирован')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Парли не совпадают')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'email']