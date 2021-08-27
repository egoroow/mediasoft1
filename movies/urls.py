from django.urls import path
from . import views
from .models import Movie, Actor, Genre, Producer
from .forms import MovieForm, ActorForm, ProducerForm, GenreForm
from django.contrib.auth.views import LogoutView

app_name = 'movies'
urlpatterns = [
    path('',views.render_index, name='index'),
    path('movie/<int:movie_id>',views.render_movie, name='render_movie'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('add/movie', views.ModelCreateView.as_view(model=Movie, form_class=MovieForm), name='add_movie'),
    path('movie/<slug:pk>/remove/', views.ModelDeleteView.as_view(model=Movie, permission_required='movies.delete_movie'), name='delete_movie'),
    path('movie/<slug:pk>/edit/', views.ModelUpdateView.as_view(model=Movie, form_class=MovieForm, permission_required='movies.change_movie'), name='update_movie'),
    path('add/actor', views.ModelCreateView.as_view(model=Actor, form_class=ActorForm), name='add_actor'),
    path('add/genre', views.ModelCreateView.as_view(model=Genre, form_class=GenreForm), name='add_genre'),
    path('add/producer', views.ModelCreateView.as_view(model=Producer, form_class=ProducerForm), name='add_producer'),
    path('search/genre/<int:genre_id>', views.search, name='search_genre'),
    path('search/actor/<int:actor_id>', views.search, name='search_actor'),
    path('search/producer/<int:producer_id>', views.search, name='search_producer'),
]
