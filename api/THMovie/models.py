from django.db import models


class Actor(models.Model):
    actor_id = models.CharField(max_length=100, primary_key=True)
    nickname_th = models.CharField(max_length=100)
    fullname_th = models.CharField(max_length=255)
    nickname_en = models.CharField(max_length=100)
    fullname_en = models.CharField(max_length=255)


class Genre(models.Model):
    genre_id = models.CharField(max_length=100, primary_key=True)
    genre_name = models.CharField(max_length=255)


class Movie(models.Model):
    movie_id = models.CharField(max_length=100, primary_key=True)
    title_th = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    release_year = models.IntegerField()


class Platform(models.Model):
    platform_id = models.CharField(max_length=100, primary_key=True)
    platform_name = models.CharField(max_length=255)


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


# Relationship between Movies and Platforms
class Available(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)


# Actors playing in movies
class Play(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)


# Audience responses, assuming a simplified structure
class Response(models.Model):
    response_id = models.CharField(max_length=100, primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    satisfaction = models.IntegerField()
