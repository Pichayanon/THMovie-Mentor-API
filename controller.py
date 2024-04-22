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


def get_movie_information(movie_id):
    """Retrieve detailed information about a specific movie, including a list of actors, genres, and platforms."""
    with pool.connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            SELECT movie_id, title_th, title_en, release_year
            FROM movies
            WHERE movie_id = %s;
        """, (movie_id,))
        movie_data = cursor.fetchone()
        if not movie_data:
            abort(404, description="Movie not found")
        movie_id, title_th, title_en, release_year = movie_data

        cursor.execute("""
            SELECT a.actor_id, a.nickname_th, a.fullname_th, a.nickname_en, a.fullname_en
            FROM actors a
            JOIN play p ON p.actor_id = a.actor_id
            WHERE p.movie_id = %s;
        """, (movie_id,))
        actors = [models.Actor(*row) for row in cursor.fetchall()]

        cursor.execute("""
            SELECT g.genre_id, g.genre_name
            FROM genres g
            JOIN moviegenre mg ON g.genre_id = mg.genre_id
            WHERE mg.movie_id = %s;
        """, (movie_id,))
        genres = [models.Genre(*row) for row in cursor.fetchall()]

        cursor.execute("""
            SELECT p.platform_id, p.platform_name
            FROM platforms p
            JOIN available a ON p.platform_id = a.platform_id
            WHERE a.movie_id = %s;
        """, (movie_id,))
        platforms = [models.Platform(*row) for row in cursor.fetchall()]

        movie = models.MovieInformation(
            movie_id=movie_id,
            title_th=title_th,
            title_en=title_en,
            release_year=release_year,
            actors=actors,
            genres=genres,
            platforms=platforms
        )
        return movie


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
            abort(404, description="No movies found for specified platform.")
        return movies


def get_platforms_for_movie(movie_id):
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
            abort(404, description="No platforms found for the specified movie.")

        platforms = [models.Platform(*row) for row in platform_rows]
        return platforms


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
            abort(404, description=f"No movies found for gender: {gender} and age: {age}.")
        return movies
