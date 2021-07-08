from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ('actor_id', 'actor_name', 'actor_surname', 'actor_patronymic')


@admin.register(models.Producer)
class ProducerAdmin(admin.ModelAdmin):
    """Режиссер"""
    list_display = ('producer_id', 'producer_name', 'producer_surname', 'producer_patronymic')


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанр"""
    list_display = ('genre_id', 'genre_title')


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильм"""
    list_display = ('movie_id', 'movie_title', 'movie_producer', 'movie_description', 'movie_trailer', 'movie_img')
