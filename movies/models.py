from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Actor(models.Model):
    """Актер"""
    actor_id = models.AutoField(primary_key=True)
    actor_name = models.CharField(max_length=100, verbose_name='Имя')
    actor_surname = models.CharField(max_length=100, verbose_name='Фамилия')
    actor_patronymic = models.CharField(max_length=100, verbose_name='Отчество')

    def __str__(self):
        fio = f'{self.actor_name} {self.actor_surname} {self.actor_patronymic}'
        return fio


class Producer(models.Model):
    """Режиссер"""
    producer_id = models.AutoField(primary_key=True)
    producer_name = models.CharField(max_length=100 , verbose_name='Имя')
    producer_surname = models.CharField(max_length=100, verbose_name='Фамилия')
    producer_patronymic = models.CharField(max_length=100, null=True, verbose_name='Отчество')

    def __str__(self):
        fio = f'{self.producer_name} {self.producer_surname} {self.producer_patronymic}'
        return fio


class Genre(models.Model):
    """Жанр фильма"""
    genre_id = models.AutoField(primary_key=True)
    genre_title = models.CharField(max_length=50, verbose_name='Название жанра')

    def __str__(self):
        return self.genre_title


class Movie(models.Model):
    """Фильм"""
    movie_id = models.AutoField(primary_key=True)
    movie_title = models.CharField(max_length=150, verbose_name='Название фильма')
    movie_genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    movie_producer = models.ForeignKey(Producer, verbose_name='Режиссер', on_delete=models.SET(None))
    movie_actor = models.ManyToManyField(Actor, verbose_name='Актеры')
    movie_description = models.TextField(verbose_name='Описание фильма')
    movie_trailer = models.TextField(verbose_name='Ссылка на трейлер', null=True)
    movie_mark = models.IntegerField(verbose_name='Оценка фильма', default=0)
    movie_img = models.TextField(verbose_name='Ссылка на обложку', null=False, default='https://xn--90achxr2b.xn--p1ai/files/no_photo3.jpg')

    def __str__(self):
        return self.movie_title
