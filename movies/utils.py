from .models import *
from .forms import *
from django.urls import reverse_lazy


class ReverseLazyMixin():
    success_url = reverse_lazy('movies:index')
    
    
class MovieMixin(ReverseLazyMixin):
    template_name = 'add.html'
    model = Movie
    form_class = MovieForm
    raise_exception = True


class ActorMixin(ReverseLazyMixin):
    template_name = 'add.html'
    model = Actor
    form_class = ActorForm
    raise_exception = True


class ProducerMixin(ReverseLazyMixin):
    template_name = 'add.html'
    model = Producer
    form_class = ProducerForm
    raise_exception = True


class GenreMixin(ReverseLazyMixin):
    template_name = 'add.html'
    model = Genre
    form_class = GenreForm
    raise_exception = True
