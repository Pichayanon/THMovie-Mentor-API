# THMovie-Mentor-API

This project involves creating an API to provide information about Thai movies, including details about specific movies.

### API Endpoints

1. Getting the list of movies and their information:
* /movies

2. Getting information about specific movies:
* /movies/{movie_id}

3. Getting the list of movies starring specific actors:
* /movies/actor/{actor_id}

4. Getting the list of movies in a specific year:
* /movies/year/{year}

5. Getting the list of movies in specific genres:
* /movies/genre/{genre}

6. Getting the list of movies popular among specific age groups:
* /movies/age/{age}

7. Getting the list of movies popular among specific genders:
* /movies/gender/{gender}
* /movies/gender/{gender}/age/{age}

8. Getting the list of movies available on a specific application:
* /movies/application/{application}

9. Getting the list of movies starring specific actors:
* /movies/actor/{actor_id}

10. Getting the list of applications where a specific where a specific movie is available:
/movies/{movie_id}/application