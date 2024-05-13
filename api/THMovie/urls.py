# urls.py
from django.urls import path
from .views import (MovieList, MovieDetail, MoviesByGenre, MoviesByActor, MoviesByPlatform,
                    MoviesByYear, MoviesByAge, MoviesByGender, MoviesByGenderAndAge,
                    GenresOfMovie, ActorsOfMovie, PlatformsOfMovie, GenresGenderCounts)

app_name = 'THMovie'

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movies-list'),
    path('movies/<str:movie_id>/', MovieDetail.as_view(), name='movie-detail'),
    path('movies/genre/<str:genre_id>/', MoviesByGenre.as_view(), name='movies-by-genre'),
    path('movies/actor/<str:actor_id>/', MoviesByActor.as_view(), name='movies-by-actor'),
    path('movies/platform/<str:platform_id>/', MoviesByPlatform.as_view(), name='movies-by-platform'),
    path('movies/year/<int:year>/', MoviesByYear.as_view(), name='movies-by-year'),
    path('movies/age/<int:age>/', MoviesByAge.as_view(), name='movies-by-age'),
    path('movies/gender/<str:gender>/', MoviesByGender.as_view(), name='movies-by-gender'),
    path('movies/gender/<str:gender>/age/<int:age>/', MoviesByGenderAndAge.as_view(), name='movies-by-gender-and-age'),
    path('genresOfMovie/<str:movie_id>/', GenresOfMovie.as_view(), name='genres-of-movie'),
    path('actorsOfMovie/<str:movie_id>/', ActorsOfMovie.as_view(), name='actors-of-movie'),
    path('platformsOfMovie/<str:movie_id>/', PlatformsOfMovie.as_view(), name='platforms-of-movie'),
    path('genres/genderCounts/', GenresGenderCounts.as_view(), name='genres-gender-counts'),
]
