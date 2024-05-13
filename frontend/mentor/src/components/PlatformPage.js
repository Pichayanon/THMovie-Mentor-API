import { useState, useEffect } from 'react';
import './AgePage.css';
import NavBar from './NavBar';
import Popup from './Popup';
import BasicCard from './Card';
import AppSearch from './AppSearch';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';

function PlatformPage() {
    const [searchText, setSearchText] = useState('');
    const [movies, setMovies] = useState([]);
    const [age, setAge] = useState(20);
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [getMovie, setGetMovie] = useState(false);
    const [error, setError] = useState('');

    function valuetext(value) {
        return `${value} years`;
    }

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/TH-Movies/movies/age/${age}`)
            .then(res => {
                if (!res.ok) {
                    throw new Error('Network response was not ok');
                }
                return res.json();
            })
            .then(resJson => {
                if (resJson.length === 0) {
                    throw new Error('No movies found for this age');
                }
                setMovies(resJson);
                setError(''); // Reset error message
            })
            .catch(err => {
                setError(err.message);
                setMovies([]); // Clear movies list
            });
    }, [age]);

    let popup = null;
    if (isPopupOpen) {
        popup = <Popup movie={getMovie} onPopupClose={() => setIsPopupOpen(false)} />;
    }

    const movieElements = movies.filter((item) => {
        return item.title_en.includes(searchText);
    }).map(movie => {
        return <BasicCard key={movie.movie_id} movie={movie} onClick={() => { setGetMovie(movie.movie_id); setIsPopupOpen(true); }} />
    });

    return (
        <div className="app">
            <NavBar />
            <AppSearch value={searchText} onValueChange={setSearchText} />


        </div>
    );
}

export default PlatformPage;
