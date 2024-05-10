from swagger_server import models
import sys
from flask import abort
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_STUB_DIR)

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)

def get_movies():
    """Retrieve all movies."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("SELECT movie_id, title_th, title_en FROM movies")
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="Movies not found.")
        return movies


def get_movie_detail(movie_id):
    """Retrieve detailed of specific movie."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT movie_id, title_th, title_en
            FROM movies
            WHERE movie_id = %s;
        """, (movie_id,))
        movie_id, title_th, title_en = cursor.fetchone()
        movie = models.Movie(movie_id, title_th, title_en)
        if not movie:
            abort(404, description="Movie not found")
        return movie


def get_genres_of_movie(movie_id):
    """Retrieve all genres for specific movie."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT g.genre_id, g.genre_name
            FROM genres g
            JOIN moviegenre mv ON mv.genre_id = g.genre_id
            WHERE mv.movie_id = %s
        """, (movie_id,))
        genre_rows = cursor.fetchall()
        if not genre_rows:
            abort(404, description="No actor found for the specified movie.")
        genres = [models.Genre(*row) for row in genre_rows]
        return genres

def get_actors_of_movie(movie_id):
    """Retrieve all actor for specific movie."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT a.actor_id, a.nickname_th, a.fullname_th, a.nickname_en, a.fullname_en
            FROM actors a
            JOIN play p ON a.actor_id = p.actor_id
            WHERE p.movie_id = %s
        """, (movie_id,))
        actor_rows = cursor.fetchall()
        if not actor_rows:
            abort(404, description="No actor found for the specified movie.")
        actors = [models.Actor(*row) for row in actor_rows]
        return actors
    
def get_platforms_of_movie(movie_id):
    """Retrieve all platforms where a specific movie is available."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT p.platform_id, p.platform_name
            FROM platforms p
            JOIN available a ON p.platform_id = a.platform_id
            WHERE a.movie_id = %s
        """, (movie_id,))
        platform_rows = cursor.fetchall()
        if not platform_rows:
            abort(404, description="No platforms found for specified movie.")
        platforms = [models.Platform(*row) for row in platform_rows]
        return platforms

def get_movies_by_actor(actor_id):
    """Retrieve all movies by a specific actor."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT m.movie_id, m.title_th, m.title_en 
            FROM movies m
            JOIN play p ON m.movie_id = p.movie_id
            WHERE p.actor_id = %s
        """, (actor_id,))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="No movies found for the specified actor.")
        return movies

def get_movies_by_age(age):
    """Retrieve all movies popular with a specific age group."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT m.movie_id, m.title_th, m.title_en 
            FROM movies m
            JOIN responses r ON m.movie_id = r.movie_id
            WHERE r.age = %s
        """, (age,))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="No movies found for the specified age.")
        return movies

def get_movies_by_gender(gender):
    """Retrieve all movies popular with a specific gender."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT m.movie_id, m.title_th, m.title_en 
            FROM movies m
            JOIN responses r ON m.movie_id = r.movie_id
            WHERE r.gender = %s
        """, (gender,))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="No movies found for the specified gender.")
        return movies

def get_movies_by_genre(genre_id):
    """Retrieve all movies of a specific genre."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT m.movie_id, m.title_th, m.title_en 
            FROM movies m
            JOIN moviegenre mg ON m.movie_id = mg.movie_id
            WHERE mg.genre_id = %s
        """, (genre_id,))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="No movies found for the specified genre.")
        return movies

def get_movies_by_gender_age(gender, age):
    """Retrieve movies popular with a specific gender and age group."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT m.movie_id, m.title_th, m.title_en
            FROM movies m
            JOIN responses r ON m.movie_id = r.movie_id
            WHERE r.gender = %s AND r.age = %s
        """, (gender, age))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(
                404, description=f"No movies found for gender: {gender} and age: {age}.")
        return moviess
    
def get_movies_by_year(year):
    """Retrieve all movies released in a specific year."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT movie_id, title_th, title_en 
            FROM movies
            WHERE release_year = %s
        """, (year,))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="No movies found for the specified year.")
        return movies

def get_movies_by_platform(platform_id):
    """Retrieve all movies available on a specific platform."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT m.movie_id, m.title_th, m.title_en 
            FROM movies m
            JOIN available a ON m.movie_id = a.movie_id
            WHERE a.platform_id = %s
        """, (platform_id),)
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="No movies found for specific platform.")
        return movies



