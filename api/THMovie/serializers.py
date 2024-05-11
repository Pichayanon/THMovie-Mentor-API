from rest_framework import serializers
from .models import Movie, Actor, Genre, Platform


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'title_th', 'title_en']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_id', 'nickname_th', 'fullname_th', 'nickname_en', 'fullname_en']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_id', 'genre_name']


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['platform_id', 'platform_name']
