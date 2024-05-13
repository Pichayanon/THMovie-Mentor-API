import React, { useState, useEffect } from 'react';
import './GenrePage.css';
import NavBar from './NavBar';
import Popup from './Popup';
import BasicCard from './Card';
import AppSearch from './AppSearch';

function GenrePage() {
    const [searchText, setSearchText] = useState('');
    const [movies, setMovies] = useState([]);
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [getMovie, setGetMovie] = useState(false);
    const [genre, setGenre] = useState('g001');
    const [error, setError] = useState('');  // Added error state to track fetch issues or empty data

    let popup = null;
    if (isPopupOpen) {
        popup = <Popup movie={getMovie} onPopupClose={() => setIsPopupOpen(false)} />;
    }

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/TH-Movies/movies/genre/${genre}`).then(res => {
            if (!res.ok) {
                throw new Error('Network response was not ok');
            }
            return res.json();
        }).then(resJson => {
            if (resJson.length === 0) {  // Check if the array is empty
                setError('No movies available in this genre.');
                setMovies([]);
            } else {
                setMovies(resJson);
                setError('');  // Clear any previous errors
            }
        }).catch(error => {
            console.error('Failed to fetch movies:', error);
            setError('Failed to fetch movies. Please try again later.');
        });
    }, [genre]);

    const movieElements = movies.filter((item) => {
        return item.title_en.includes(searchText);
    }).map(movie => {
        return <BasicCard movie={movie} onClick={() => {setGetMovie(movie.movie_id); setIsPopupOpen(true);} }/>
    });


    return (
        <div className="app">
            <NavBar/>
            <AppSearch value={searchText} onValueChange={setSearchText}/>
            <div className='selector'>
                <select value={genre} onChange={(e) => setGenre(e.target.value)} className="genre-select">
                    <option value="g001">Action</option>
                    <option value="g002">Comedy</option>
                    <option value="g003">Drama</option>
                    <option value="g004">Romance</option>
                    <option value="g005">Adventure</option>
                    <option value="g006">Crime</option>
                    <option value="g007">Fantasy</option>
                    <option value="g008">History</option>
                    <option value="g009">Horror</option>
                    <option value="g010">Mystery</option>
                    <option value="g011">Sci-Fi</option>
                    <option value="g012">Thriller</option>
                </select>
            </div>
            <section className="app-section">
                <div className="app-container">
                    <div className="app-grid">
                        {movieElements.length > 0 ? movieElements : <div>{error || 'No movies found.'}</div>}
                    </div>
                </div>
                {popup}
            </section>
        </div>
    );
}

export default GenrePage;
