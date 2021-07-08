from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import UpdateView, DeleteView, View, CreateView

from .models import *
from movies.forms import *
# Create your views here.


def render_index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies':movies})


def render_movie(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    return render(request, 'movie.html', {'movie':movie})


def search(request, genre_id=None, actor_id=None, producer_id=None):
    error = ''
    movies = []
    if genre_id:
        movies = Movie.objects.filter(movie_genre=genre_id)
    elif actor_id:
        movies = Movie.objects.filter(movie_actor=actor_id)
    elif producer_id:
        movies = Movie.objects.filter(movie_producer=producer_id)
    if len(movies) == 0:
        error = 'Фильмы не найдены'
    return render(request, 'index.html', {'movies': movies, 'error': error})


class ActorCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add.html'
    form_class = ActorForm
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class ActorUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    template_name = 'add.html'
    model = Actor
    form_class = ActorForm
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class ActorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'add.html'
    model = Actor
    form_class = ActorForm
    permission_required = 'movies.delete_actor'
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class ProducerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add.html'
    form_class = ProducerForm
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class ProducerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'add.html'
    model = Producer
    form_class = ProducerForm
    permission_required = 'movies.change_producer'
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class ProducerDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    template_name = 'add.html'
    model = Producer
    form_class = ProducerForm
    permission_required = 'movies.delete_producer'
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class GenreCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add.html'
    form_class = GenreForm
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class GenreUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    template_name = 'add.html'
    model = Genre
    form_class = GenreForm
    permission_required = 'movies.change_genre'
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class GenreDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    template_name = 'add.html'
    model = Genre
    form_class = GenreForm
    permission_required = 'movies.delete_genre'
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add.html'
    form_class = MovieForm

    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class MovieUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    template_name = 'add.html'
    model = Movie
    form_class = MovieForm
    permission_required = 'movies.change_movie'
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class MovieDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    template_name = 'add.html'
    model = Movie
    form_class = MovieForm
    permission_required = 'movies.delete_movie'
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('movies:index')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        return render(request, 'login.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'login.html', {'form':form})


class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        return render(request, 'registration.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'registration.html', {'form': form})