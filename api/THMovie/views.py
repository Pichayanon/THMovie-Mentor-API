# views.py
from django.http import Http404
from rest_framework import generics
from .models import Movie, Actor, Genre, Platform
from .serializers import MovieSerializer, ActorSerializer, GenreSerializer, PlatformSerializer, GenreGenderCountSerializer


class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'movie_id'


class MoviesByGenre(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.filter(moviegenre__genre_id=self.kwargs['genre_id'])
        if not queryset:
            raise Http404("No movies found for the specified platform.")
        return queryset


class MoviesByActor(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.filter(play__actor_id=self.kwargs['actor_id'])
        if not queryset:
            raise Http404("No movies found for the specified platform.")
        return queryset


class MoviesByPlatform(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.filter(available__platform_id=self.kwargs['platform_id'])
        if not queryset:
            raise Http404("No movies found for the specified platform.")
        return queryset


class MoviesByYear(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.filter(release_year=self.kwargs['year'])
        if not queryset:
            raise Http404("No movies found for the specified platform.")
        return queryset


class MoviesByAge(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.filter(response__age=self.kwargs['age']).distinct()
        if not queryset:
            raise Http404("No movies found for the specified platform.")
        return queryset


class MoviesByGender(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.filter(response__gender=self.kwargs['gender']).distinct()
        if not queryset:
            raise Http404("No movies found for the specified platform.")
        return queryset


class MoviesByGenderAndAge(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.filter(response__gender=self.kwargs['gender'], response__age=self.kwargs['age']).distinct()
        if not queryset:
            raise Http404("No movies found for the specified platform.")
        return queryset


class GenresOfMovie(generics.ListAPIView):
    serializer_class = GenreSerializer

    def get_queryset(self):
        queryset = Genre.objects.filter(moviegenre__movie_id=self.kwargs['movie_id'])
        if not queryset:
            raise Http404("No movies found for the specified platform.")
        return queryset


class ActorsOfMovie(generics.ListAPIView):
    serializer_class = ActorSerializer

    def get_queryset(self):
        queryset = Actor.objects.filter(play__movie_id=self.kwargs['movie_id'])
        if not queryset:
            raise Http404("No movies found for the specified platform.")
        return queryset


class PlatformsOfMovie(generics.ListAPIView):
    serializer_class = PlatformSerializer

    def get_queryset(self):
        queryset = Platform.objects.filter(available__movie_id=self.kwargs['movie_id'])
        if not queryset:
            raise Http404("No movies found for the specified platform.")
        return queryset


class GenresGenderCounts(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreGenderCountSerializer
