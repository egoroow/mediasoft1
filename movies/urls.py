from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'movies'
urlpatterns = [
    path('',views.render_index, name='index'),
    path('movie/<int:movie_id>',views.render_movie, name='render_movie'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('add/movie', views.MovieCreateView.as_view(), name='add_movie'),
    path('movie/<slug:pk>/remove/', views.MovieDeleteView.as_view(), name='delete_movie'),
    path('movie/<slug:pk>/edit/', views.MovieUpdateView.as_view(), name='update_movie'),
    path('add/actor', views.ActorCreateView.as_view(), name='add_actor'),
    path('actor/<slug:pk>/remove/', views.ActorDeleteView.as_view(), name='delete_actor'),
    path('actor/<slug:pk>/edit/', views.ActorUpdateView.as_view(), name='update_actor'),
    path('add/genre', views.GenreCreateView.as_view(), name='add_genre'),
    path('genre/<slug:pk>/remove/', views.GenreDeleteView.as_view(), name='delete_genre'),
    path('genre/<slug:pk>/edit/', views.GenreUpdateView.as_view(), name='update_genre'),
    path('add/producer', views.ProducerCreateView.as_view(), name='add_producer'),
    path('producer/<slug:pk>/remove/', views.ProducerDeleteView.as_view(), name='delete_producer'),
    path('producer/<slug:pk>/edit/', views.ProducerUpdateView.as_view(), name='update_producer'),
    path('search/genre/<int:genre_id>', views.search, name='search_genre'),
    path('search/actor/<int:actor_id>', views.search, name='search_actor'),
    path('search/producer/<int:producer_id>', views.search, name='search_producer'),
]