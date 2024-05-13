import React, { useState, useEffect } from 'react';
import './App.css';
import NavBar from './components/NavBar';
import Popup from './components/Popup';
import BasicCard from './components/Card';
import AppSearch from './components/AppSearch';

function App() {
    const [searchText, setSearchText] = useState('');
    const [age, setAge] = useState('');
    const [tempAge, setTempAge] = useState(''); // Temporary age for submission
    const [gender, setGender] = useState('');
    const [movies, setMovies] = useState([]);
    const [isPopupOpen, SetIsPopupOpen] = useState(false);
    const [getMovie, setGetMovie] = useState(false);

    useEffect(() => {
        let url = 'http://127.0.0.1:8000/TH-Movies/movies/';
        if (age && gender) {
            url += `gender/${gender}/age/${age}/`;
        } else if (age) {
            url += `age/${age}/`;
        } else if (gender) {
            url += `gender/${gender}/`;
        }

        fetch(url).then(res => res.json()).then(resJson => {
            // Check if the response is not null and is an array before setting it
            if (resJson && Array.isArray(resJson)) {
                setMovies(resJson);
            } else {
                console.log("Received null or invalid response");
                setMovies([]); // Set movies to an empty array if response is null or not an array
            }
        }).catch(err => {
            console.error("Failed to fetch movies:", err);
            setMovies([]); // Set movies to an empty array on fetch error
        });
    }, [age, gender]);

    const handleSubmitAge = () => {
        setAge(tempAge);
    };

    let popup = null;
    if (isPopupOpen) {
        popup = <Popup movie={getMovie} onPopupClose={() => SetIsPopupOpen(false)} />;
    }

    const movieElements = movies.filter((item) => {
        return item.title_en.toLowerCase().includes(searchText.toLowerCase());
    }).map(movie => {
        return <BasicCard key={movie.movie_id} movie={movie} onClick={() => { setGetMovie(movie.movie_id); SetIsPopupOpen(true); }} />
    });

    return (
        <div className="app">
            <NavBar/>
            <AppSearch value={searchText} onValueChange={setSearchText}/>
            <div className="filter-container">
                <input
                    type="text"
                    placeholder="Input Your Age"
                    value={tempAge}
                    onChange={e => setTempAge(e.target.value)}
                    className='age-input'
                />
                <button onClick={handleSubmitAge} className='age-submit'>Submit Age</button>
                <select
                    value={gender}
                    onChange={e => setGender(e.target.value)}
                    className="gender-select">
                    <option value="">Gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                </select>
            </div>
            <section className="app-section">
                <div className="app-container">
                    <div className="app-grid">
                        {movieElements.length > 0 ? movieElements : <p>No movies in the database.</p>}
                    </div>
                </div>
                {popup}
            </section>
        </div>
    );
}

export default App;
