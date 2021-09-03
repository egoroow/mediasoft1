from .models import *
from .forms import *


class MovieMixin():
    template_name = 'add.html'
    model = Movie
    form_class = MovieForm
    raise_exception = True


class ActorMixin():
    template_name = 'add.html'
    model = Actor
    form_class = ActorForm
    raise_exception = True


class ProducerMixin():
    template_name = 'add.html'
    model = Producer
    form_class = ProducerForm
    raise_exception = True


class GenreMixin():
    template_name = 'add.html'
    model = Genre
    form_class = GenreForm
    raise_exception = True