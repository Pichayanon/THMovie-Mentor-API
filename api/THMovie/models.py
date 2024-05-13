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

    def gender_counts(self):
        gender_dict = {'male': 0, 'female': 0}
        movies = Movie.objects.filter(moviegenre__genre=self)
        responses = Response.objects.filter(movie__in=movies).values('gender').annotate(count=models.Count('gender'))
        for response in responses:
            if response['gender'].lower() in gender_dict:
                gender_dict[response['gender'].lower()] = response['count']
        return gender_dict


class Movie(models.Model):
    movie_id = models.CharField(max_length=100, primary_key=True)
    title_th = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    release_year = models.IntegerField()
    type = models.CharField(max_length=255)


class Platform(models.Model):
    platform_id = models.CharField(max_length=100, primary_key=True)
    platform_name = models.CharField(max_length=255)


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Available(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)


class Play(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)


class Response(models.Model):
    response_id = models.CharField(max_length=100, primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    satisfaction = models.IntegerField()
