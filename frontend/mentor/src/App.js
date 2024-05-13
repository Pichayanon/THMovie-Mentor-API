import { useState, useEffect } from 'react';
import './App.css';
import NavBar from './components/NavBar';
import Popup from './components/Popup';
import BasicCard from './components/Card';
import AppSearch from './components/AppSearch';


function App() {
    const [searchText, setSearchText] = useState('');
    const [movies, setMovies] = useState([]);
    const [isPopupOpen, SetIsPopupOpen] = useState(false);
    const [getMovie, setGetMovie] = useState(false);

    let popup = null;
    if (isPopupOpen) {
        popup = <Popup movie={getMovie} onPopupClose={() => SetIsPopupOpen(false)} />;
    }

    useEffect(() => {
        fetch('http://127.0.0.1:8000/TH-Movies/movies/').then(res => {
            return res.json();
        }).then(resJson => {
            setMovies(resJson);
        });
    }, []);

    const movieElements = movies.filter((item) => {
        return item.title_en.includes(searchText);
    }).map(movie => {
        return <BasicCard movie={movie} onClick={() => {setGetMovie(movie.movie_id); SetIsPopupOpen(true)} }/>
    });
   
    return (
        <div className="app">
            <NavBar/>
            <AppSearch value={searchText} onValueChange={setSearchText}/>
            <section className="app-section">
                <div className="app-container">
                    <div className="app-grid">
                        {movieElements}
                    </div>
                </div>
                {popup}
            </section>
        </div>
    );
}

export default App;
