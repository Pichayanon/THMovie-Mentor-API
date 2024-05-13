import { useState, useEffect } from 'react';
import './PlatformPage.css';
import NavBar from './NavBar';
import Popup from './Popup';
import BasicCard from './Card';
import AppSearch from './AppSearch';
import Box from '@mui/material/Box';

function PlatformPage() {
    const [searchText, setSearchText] = useState('');
    const [movies, setMovies] = useState([]);
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [getMovie, setGetMovie] = useState(false);
    const [platform, setPlatform] = useState('p001');
    const [error, setError] = useState('');

    let popup = null;
    if (isPopupOpen) {
        popup = <Popup movie={getMovie} onPopupClose={() => setIsPopupOpen(false)} />;
    }

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/TH-Movies/movies/platform/${platform}`).then(res => {
            if (!res.ok) {
                throw new Error('Network response was not ok');
            }
            return res.json();
        }).then(resJson => {
            if (resJson.length === 0) {
                setError('No movies available on this platform.');
                setMovies([]);
            } else {
                setMovies(resJson);
                setError('');  // Clear any previous errors
            }
        }).catch(error => {
            console.error('Failed to fetch movies:', error);
            setError('Failed to fetch movies. Please try again later.');
        });
    }, [platform]);

    const movieElements = movies.filter((item) => {
        return item.title_en.includes(searchText);
    }).map(movie => {
        return <BasicCard key={movie.movie_id} movie={movie} onClick={() => { setGetMovie(movie.movie_id); setIsPopupOpen(true); }} />
    });

    return (
        <div className="app">
            <NavBar />
            <AppSearch value={searchText} onValueChange={setSearchText} />
            <div className='selector'>
                <select value={platform} onChange={(e) => setPlatform(e.target.value)} className="platform-select">
                    <option value="p001">Prime Video</option>
                    <option value="p002">Apple TV</option>
                    <option value="p003">Netflix</option>
                    <option value="p004">Viu</option>
                    <option value="p005">YouTube</option>
                    <option value="p006">3ch Plus</option>
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

export default PlatformPage;