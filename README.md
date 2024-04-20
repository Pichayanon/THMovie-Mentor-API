# THMovie-Mentor-API

This project involves creating an API that provides information about Thai movies and their details. We collect data through a questionnaire asking people of various ages and genders about their favorite Thai movies.   After obtaining the movie titles, we use web scraping to find out when they were released and where they can be watched. These applications include Prime Video, Apple TV, Netflix, VIU, YouTube, and 3CHPlus, which are popular among Thai audiences for watching Thai movies.

## API Endpoints

##### 1. Getting the list of movies and their information:
* /movies

##### 2. Getting information about specific movies:
* /movies/{movie_id}

##### 3. Getting the list of movies starring specific actors:
* /movies/actor/{actor_id}

##### 4. Getting the list of movies in a specific year:
* /movies/year/{year}

##### 5. Getting the list of movies in specific genres:
* /movies/genre/{genre}

##### 6. Getting the list of movies popular among specific age:
* /movies/age/{age}

##### 7. Getting the list of movies popular among specific genders:
* /movies/gender/{gender}
* /movies/gender/{gender}/age/{age}

##### 8. Getting the list of movies available on a specific application:
* /movies/application/{application}

##### 9. Getting the list of applications where a specific where a specific movie is available:
* /movies/{movie_id}/application
