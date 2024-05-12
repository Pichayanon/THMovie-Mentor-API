from django.test import TestCase
from rest_framework.test import APIClient
from .models import Movie, Actor, Genre, Platform, Response, MovieGenre, Play, Available


class BaseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create movies
        self.movie1 = Movie.objects.create(movie_id="m001", title_th="หนัง 1", title_en="movie 1", release_year=2022, type="tv-series")
        self.movie2 = Movie.objects.create(movie_id="m002", title_th="หนัง 2", title_en="movie 2", release_year=2022, type="tv-series")
        self.movie3 = Movie.objects.create(movie_id="m003", title_th="หนัง 3", title_en="movie 3", release_year=2023, type="movie")

        # Create actors
        self.actor1 = Actor.objects.create(actor_id="a001", nickname_th="ชื่อเล่นนักแสดง 1", fullname_th="ชื่อจริงนักแสดง 1",
                                           nickname_en="Nickname actor 1", fullname_en="Fullname actor 1")
        self.actor2 = Actor.objects.create(actor_id="a002", nickname_th="ชื่อเล่นนักแสดง 2", fullname_th="ชื่อจริงนักแสดง 2",
                                           nickname_en="Nickname actor 2", fullname_en="Fullname actor 2")

        # Create genres
        self.genre1 = Genre.objects.create(genre_id="g001", genre_name="Comedy")
        self.genre2 = Genre.objects.create(genre_id="g002", genre_name="Action")

        # Create platforms
        self.platform1 = Platform.objects.create(platform_id="p001", platform_name="Netflix")
        self.platform2 = Platform.objects.create(platform_id="p002", platform_name="Youtube")

        # Create responses
        self.response1 = Response.objects.create(response_id="r001", movie_id=self.movie1.movie_id,
                                                 actor_id=self.actor1.actor_id, gender="male", age=25, satisfaction=5)
        self.response2 = Response.objects.create(response_id="r002", movie_id=self.movie1.movie_id,
                                                 actor_id=self.actor2.actor_id, gender="female", age=30, satisfaction=4)
        self.response3 = Response.objects.create(response_id="r003", movie_id=self.movie2.movie_id,
                                                 actor_id=self.actor2.actor_id, gender="male", age=35, satisfaction=4)

        MovieGenre.objects.create(movie_id=self.movie1.movie_id, genre_id=self.genre1.genre_id)
        MovieGenre.objects.create(movie_id=self.movie2.movie_id, genre_id=self.genre2.genre_id)
        MovieGenre.objects.create(movie_id=self.movie3.movie_id, genre_id=self.genre1.genre_id)
        MovieGenre.objects.create(movie_id=self.movie3.movie_id, genre_id=self.genre2.genre_id)

        Play.objects.create(movie_id=self.movie1.movie_id, actor_id=self.actor1.actor_id)
        Play.objects.create(movie_id=self.movie1.movie_id, actor_id=self.actor2.actor_id)
        Play.objects.create(movie_id=self.movie2.movie_id, actor_id=self.actor2.actor_id)
        Play.objects.create(movie_id=self.movie3.movie_id, actor_id=self.actor1.actor_id)

        Available.objects.create(movie=self.movie1, platform=self.platform1)
        Available.objects.create(movie_id=self.movie2.movie_id, platform_id=self.platform2.platform_id)
        Available.objects.create(movie_id=self.movie3.movie_id, platform_id=self.platform1.platform_id)
        Available.objects.create(movie_id=self.movie3.movie_id, platform_id=self.platform2.platform_id)


class TestRetrieveListAllMovie(BaseTestCase):
    def test_get_all_movie(self):
        """Test case to verify request all movies

        Retrieve a list of all movies
        """
        response = self.client.get("/TH-Movies/movies/")
        self.assertEqual(response.status_code, 200)


class TestRetrieveMovieInformation(BaseTestCase):
    def test_get_valid_movie_detail(self):
        """Test case to verify request specific movies with valid movie

        Get a movie information for specific movie
        """
        response = self.client.get(f"/TH-Movies/movies/{self.movie1.movie_id}/")
        self.assertTrue(response.status_code, 200)

        expected_data = {
            'movie_id': self.movie1.movie_id,
            'title_th': self.movie1.title_th,
            'title_en': self.movie1.title_en,
            'release_year': self.movie1.release_year,
            'type': self.movie1.type
        }
        self.assertEqual(response.json(), expected_data)

    def test_get_invalid_movie_detail(self):
        """Test case to verify request specific movies with invalid movie"""
        response = self.client.get("/TH-Movies/movies/m999/")
        self.assertEqual(response.status_code, 404)


class TestRetrieveMovieByGender(BaseTestCase):
    def test_get_movies_by_valid_gender(self):
        """Test case to verify request list movies for with valid gender

        Get a list of movies popular with a specific gender
        """
        response = self.client.get(f"/TH-Movies/movies/gender/{self.response2.gender}/")
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {
                'movie_id': self.movie1.movie_id,
                'title_th': self.movie1.title_th,
                'title_en': self.movie1.title_en,
                'release_year': self.movie1.release_year,
                'type': self.movie1.type
            }
        ]
        self.assertEqual(response.json(), expected_data)

    def test_get_movies_by_invalid_gender(self):
        """Test case to verify request list movies for with invalid gender"""
        response = self.client.get('/TH-Movies/movies/gender/999/')
        self.assertEqual(response.status_code, 404)


class TestRetrieveMovieByAge(BaseTestCase):
    def test_get_movies_by_valid_age(self):
        """Test case to verify request list movies for with valid age

        Get a list of movies popular with a specific age
        """
        response = self.client.get(f"/TH-Movies/movies/age/{self.response2.age}/")
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {
                'movie_id': self.movie1.movie_id,
                'title_th': self.movie1.title_th,
                'title_en': self.movie1.title_en,
                'release_year': self.movie1.release_year,
                'type': self.movie1.type
            }
        ]
        self.assertEqual(response.json(), expected_data)

    def test_get_movies_by_invalid_age(self):
        """Test case to verify request list movies for with invalid age"""
        response = self.client.get("/TH-Movies/movies/age/999/")
        self.assertEqual(response.status_code, 404)


class TestRetrieveMovieByPlatform(BaseTestCase):
    def test_get_movies_by_valid_platform(self):
        """Test case to verify request list movies for with valid platform

        Get a list of movies available on a specific platform
        """
        response = self.client.get(f"/TH-Movies/movies/platform/{self.platform1.platform_id}/")
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {
                'movie_id': self.movie1.movie_id,
                'title_th': self.movie1.title_th,
                'title_en': self.movie1.title_en,
                'release_year': self.movie1.release_year,
                'type': self.movie1.type
            },
            {
                'movie_id': self.movie3.movie_id,
                'title_th': self.movie3.title_th,
                'title_en': self.movie3.title_en,
                'release_year': self.movie3.release_year,
                'type': self.movie3.type
            },
        ]
        self.assertEqual(response.json(), expected_data)

    def test_get_movies_by_invalid_platform(self):
        """Test case to verify request list movies for with invalid platform"""
        response = self.client.get("/TH-Movies/movies/platform/p999/")
        self.assertEqual(response.status_code, 404)


class TestRetrieveMovieByActor(BaseTestCase):
    def test_get_movies_by_valid_actor(self):
        """Test case to verify request list movies for with valid actor

        Get a list of movies starring a specific actor
        """
        response = self.client.get(f"/TH-Movies/movies/actor/{self.actor1.actor_id}/")
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {
                'movie_id': self.movie1.movie_id,
                'title_th': self.movie1.title_th,
                'title_en': self.movie1.title_en,
                'release_year': self.movie1.release_year,
                'type': self.movie1.type
            },
            {
                'movie_id': self.movie3.movie_id,
                'title_th': self.movie3.title_th,
                'title_en': self.movie3.title_en,
                'release_year': self.movie3.release_year,
                'type': self.movie3.type
            },
        ]
        self.assertEqual(response.json(), expected_data)

    def test_get_movies_by_invalid_actor(self):
        """Test case to verify request list movies for with invalid actor"""
        response = self.client.get('/TH-Movies/movies/actor/a999/')
        self.assertEqual(response.status_code, 404)


class TestRetrieveMovieByGenre(BaseTestCase):
    def test_get_movies_by_valid_genre(self):
        """Test case to verify request list movies for with valid genre

        Get a list of movies of a specific genre
        """
        response = self.client.get(f"/TH-Movies/movies/genre/{self.genre1.genre_id}/")
        self.assertEqual(response.status_code, 200)
        expected_data = [
            {
                'movie_id': self.movie1.movie_id,
                'title_th': self.movie1.title_th,
                'title_en': self.movie1.title_en,
                'release_year': self.movie1.release_year,
                'type': self.movie1.type
            },
            {
                'movie_id': self.movie3.movie_id,
                'title_th': self.movie3.title_th,
                'title_en': self.movie3.title_en,
                'release_year': self.movie3.release_year,
                'type': self.movie3.type
            },
        ]
        self.assertEqual(response.json(), expected_data)

    def test_get_movies_by_invalid_genre(self):
        """Test case to verify request list movies for with invalid genre

        Get a list of movies of a specific genre
        """
        response = self.client.get('/TH-Movies/movies/genre/g999/')
        self.assertEqual(response.status_code, 404)


class TestRetrieveMovieByYear(BaseTestCase):
    def test_get_movies_by_valid_year(self):
        """Test case to verify request list movies for with valid year

        Get a list of movies released in a specific year
        """
        response = self.client.get(f"/TH-Movies/movies/year/{self.movie1.release_year}/")
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {
                'movie_id': self.movie1.movie_id,
                'title_th': self.movie1.title_th,
                'title_en': self.movie1.title_en,
                'release_year': self.movie1.release_year,
                'type': self.movie1.type
            },
            {
                'movie_id': self.movie2.movie_id,
                'title_th': self.movie2.title_th,
                'title_en': self.movie2.title_en,
                'release_year': self.movie2.release_year,
                'type': self.movie2.type
            },
        ]
        self.assertEqual(response.json(), expected_data)

    def test_get_movies_by_invalid_year(self):
        """Test case to verify request list movies for with valid year

        Get a list of movies released in a specific year
        """
        response = self.client.get("/TH-Movies/movies/year/2050/")
        self.assertEqual(response.status_code, 404)


class TestRetrieveMovieByGenderAge(BaseTestCase):
    def test_controller_get_movies_by_valid_gender_valid_age(self):
        """Test case to verify request list movies for with valid age and gender

        Get a list of movies popular with a specific gender and age
        """
        response = self.client.get(f"/TH-Movies/movies/gender/{self.response2.gender}/age/{self.response2.age}/")
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {
                'movie_id': self.movie1.movie_id,
                'title_th': self.movie1.title_th,
                'title_en': self.movie1.title_en,
                'release_year': self.movie1.release_year,
                'type': self.movie1.type
            },
        ]
        self.assertEqual(response.json(), expected_data)

    def test_controller_get_movies_by_valid_gender_invalid_age(self):
        """Test case to verify request list movies for with valid age and invalid gender"""
        response = self.client.get("/TH-Movies/movies/gender/male/age/999/")
        self.assertEqual(response.status_code, 404)

    def test_controller_get_movies_by_invalid_gender_valid_age(self):
        """Test case to verify request list movies for with invalid age and valid gender"""
        response = self.client.get("/TH-Movies/movies/gender/abc/age/25/")
        self.assertEqual(response.status_code, 404)

    def test_controller_get_movies_by_invalid_gender_invalid_age(self):
        """Test case to verify request list movies for with invalid age and gender"""
        response = self.client.get("/TH-Movies/movies/gender/abc/age/999/")
        self.assertEqual(response.status_code, 404)


class TestRetrieveActorByMovie(BaseTestCase):
    def test_get_actors_of_valid_movie(self):
        """Test case to verify request list actor with valid movie

        Get a list of actor for specific movie
        """
        response = self.client.get(f"/TH-Movies/actorsOfMovie/{self.movie1.movie_id}/")
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {
                'actor_id': self.actor1.actor_id,
                'nickname_th': self.actor1.nickname_th,
                'fullname_th': self.actor1.fullname_th,
                'nickname_en': self.actor1.nickname_en,
                'fullname_en': self.actor1.fullname_en
            },
            {
                'actor_id': self.actor2.actor_id,
                'nickname_th': self.actor2.nickname_th,
                'fullname_th': self.actor2.fullname_th,
                'nickname_en': self.actor2.nickname_en,
                'fullname_en': self.actor2.fullname_en
            },
        ]
        self.assertEqual(response.json(), expected_data)

    def test_get_actors_of_invalid_movie(self):
        """Test case to verify request list actor with invalid movie"""
        response = self.client.get("/TH-Movies/actorsOfMovie/m999/")
        self.assertEqual(response.status_code, 404)


class TestRetrieveGenreByMovie(BaseTestCase):
    def test_get_genres_of_valid_movie(self):
        """Test case to verify request list genre with valid movie

        Get a list of movies of a specific genre
        """
        response = self.client.get(f"/TH-Movies/genresOfMovie/{self.movie1.movie_id}/")
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {
                'genre_id': self.genre1.genre_id,
                'genre_name': self.genre1.genre_name,
            },
        ]
        self.assertEqual(response.json(), expected_data)

    def test_get_genres_of_invalid_movie(self):
        """Test case to verify request list genre with invalid movie"""
        response = self.client.get("/TH-Movies/genresOfMovie/999/")
        self.assertEqual(response.status_code, 404)


class TestRetrievePlatformByMovie(BaseTestCase):
    def test_get_platforms_of_valid_movie(self):
        """Test case to verify request list platform with valid movie

        Get a list of platforms where a specific movie is available
        """
        response = self.client.get(f"/TH-Movies/platformsOfMovie/{self.movie1.movie_id}/")
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {
                'platform_id': self.platform1.platform_id,
                'platform_name': self.platform1.platform_name,
            },
        ]
        self.assertEqual(response.json(), expected_data)

    def test_get_platforms_of_invalid_movie(self):
        """Test case to verify request list platform with invalid movie"""
        response = self.client.get('/TH-Movies/platformsOfMovie/m999/')
        self.assertEqual(response.status_code, 404)
