from django.contrib import admin
from .models import Actor, Genre, Movie, Platform, MovieGenre, Available, Play, Response

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Platform)
admin.site.register(MovieGenre)
admin.site.register(Available)
admin.site.register(Play)
admin.site.register(Response)
