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
        cursor.execute("SELECT movie_id, title_th, title_en FROM Movies")
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="Movies not found.")
        return movies


def get_movie_detail(movie_id):
    """Retrieve detailed information about a specific movie, including a list of actors, genres, and platforms."""
    with pool.connection() as conn, conn.cursor() as cursor:

        cursor.execute("""
            SELECT movie_id, title_th, title_en, release_year 
            FROM Movies 
            WHERE movie_id = %s
        """, (movie_id,))
        movie = cursor.fetchone()

        if not movie:
            abort(404, description=f"Movie not found.")

        cursor.execute("""
            SELECT a.actor_id, a.nickname_th, a.fullname_th, a.nickname_en, a.fullname_en 
            FROM Actors a 
            JOIN Plays p ON p.actor_id = a.actor_id 
            WHERE p.movie_id = %s
        """, (movie_id,))
        actors = [models.Actor(*actor_row) for actor_row in cursor.fetchall()]

        cursor.execute("""
            SELECT action, comedy, drama, romance, adventure, crime, fantasy, history, horror, mystery, scifi, thriller, other 
            FROM Genres 
            WHERE movie_id = %s
        """, (movie_id,))
        genre = models.Genre(*cursor.fetchone())

        cursor.execute("""
            SELECT youtube, 3ch_plus, prime_video, apple_tv, netflix 
            FROM Platforms 
            WHERE movie_id = %s
        """, (movie_id,))
        platforms = models.Platform(*cursor.fetchone())

        detail_movie = models.DetailMovie(
            movie_id=movie[0],
            title_th=movie[1],
            title_en=movie[2],
            release_year=movie[3],
            actors=actors,
            genre=genre,
            platforms=platforms
        )
        return detail_movie


def get_movies_by_actor(actor_id):
    """Retrieve all movies by a specific actor."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT m.movie_id, m.title_th, m.title_en 
            FROM Movies m
            JOIN Plays p ON m.movie_id = p.movie_id
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
            FROM Movies m
            JOIN Responses r ON m.movie_id = r.movie_id
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
            FROM Movies m
            JOIN Responses r ON m.movie_id = r.movie_id
            WHERE r.gender = %s
        """, (gender,))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="No movies found for the specified gender.")
        return movies


def get_movies_by_genre(genre):
    """Retrieve all movies of a specific genre."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT m.movie_id, m.title_th, m.title_en 
            FROM Movies m
            JOIN Genres g ON m.movie_id = g.movie_id
            WHERE g.%s = 1
        """, (genre,))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="No movies found for the specified genre.")
        return movies


def get_movies_by_year(year):
    """Retrieve all movies released in a specific year."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT movie_id, title_th, title_en 
            FROM Movies
            WHERE release_year = %s
        """, (year,))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="No movies found for the specified year.")
        return movies


def get_movies_by_platform(application):
    """Retrieve all movies available on a specific platform."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT m.movie_id, m.title_th, m.title_en
            FROM Movies m
            JOIN Platforms p ON m.movie_id = p.movie_id
            WHERE p.%s = 1
        """, (application,))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(404, description="No movies found for specified application.")
        return movies


def get_platforms_for_movie(movie_id):
    """Retrieve all platforms where a specific movie is available."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT youtube, 3ch_plus, prime_video, apple_tv, netflix 
            FROM Platforms 
            WHERE movie_id = %s
        """, (movie_id,))
        platforms = models.Platform(*cursor.fetchone())
        return platforms


def get_movies_by_gender_age(gender, age):
    """Retrieve movies popular with a specific gender and age group."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT m.movie_id, m.title_th, m.title_en
            FROM Movies m
            JOIN Responses r ON m.movie_id = r.movie_id
            WHERE r.gender = %s AND r.age = %s
        """, (gender, age))
        movies = [models.Movie(*row) for row in cursor.fetchall()]
        if not movies:
            abort(
                404, description=f"No movies found for gender: {gender} and age: {age}.")
        return movies
