from .models import *
from .forms import *
from django.urls import reverse_lazy


class MovieMixin():
    template_name = 'add.html'
    model = Movie
    form_class = MovieForm
    raise_exception = True
    success_url = reverse_lazy('movies:index')


class ActorMixin():
    template_name = 'add.html'
    model = Actor
    form_class = ActorForm
    raise_exception = True
    success_url = reverse_lazy('movies:index')


class ProducerMixin():
    template_name = 'add.html'
    model = Producer
    form_class = ProducerForm
    raise_exception = True
    success_url = reverse_lazy('movies:index')


class GenreMixin():
    template_name = 'add.html'
    model = Genre
    form_class = GenreForm
    raise_exception = True
    success_url = reverse_lazy('movies:index')
