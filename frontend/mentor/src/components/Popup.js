import { useEffect, useState } from "react";
import './Popup.css';
import CardMedia from '@mui/material/CardMedia';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';


function Popup(props) {
    const { movie, onPopupClose } = props;
    const [movieData, setMovieData] = useState(null);
    const [actors, setActors] = useState([]);
    const [genres, setGenres] = useState([]);
    const [platforms, setPlatforms] = useState([]);

    useEffect(() => {
        document.documentElement.style.overflowY = 'hidden';
        return () => {
            document.documentElement.style.overflowY = 'auto';
        }
    }, []);

    const fetchData = async (url) => {
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Failed to fetch data:', error);
            return null; // Return null if there's an error
        }
    }

    useEffect(() => {
        fetchData(`http://127.0.0.1:8000/TH-Movies/movies/${movie}`)
            .then(data => {
                if (data) setMovieData(data);
            });
    }, [movie]);

    useEffect(() => {
        fetchData(`http://127.0.0.1:8000/TH-Movies/genresOfMovie/${movie}`)
            .then(data => {
                if (data) setGenres(data);
            });
    }, [movie]);

    useEffect(() => {
        fetchData(`http://127.0.0.1:8000/TH-Movies/actorsOfMovie/${movie}`)
            .then(data => {
                if (data) setActors(data);
            });
    }, [movie]);

    useEffect(() => {
        fetchData(`http://127.0.0.1:8000/TH-Movies/platformsOfMovie/${movie}`)
            .then(data => {
                if (data) setPlatforms(data);
            });
    }, [movie]);

    return <div className="popup" onClick={onPopupClose}>
        <Card sx={{ minWidth: 275 }} style={{ margin: 80}} className="info-card">
            <CardContent>
                {movieData ? (
                    <>
                        <Typography gutterBottom variant="h4" component="div">
                            {movieData.title_en}
                        </Typography>
                        <Typography variant="h6" color="text.secondary">
                            {movieData.title_th} - {movieData.release_year}
                        </Typography>
                    </>
                ) : (
                    <Typography gutterBottom variant="h5" component="div">
                        Loading movie details or movie not found...
                    </Typography>
                )}
                <Typography variant="body1">
                    Top Actors:
                    {actors.length > 0 ? actors.map(actor => (
                        <li key={actor.actor_id}>
                            {actor.fullname_en} ({actor.nickname_en})
                        </li>
                    )) : "No actors found."}
                </Typography>
                <Typography variant="body1">
                    Genres:
                    {genres.length > 0 ? genres.map(genre => (
                        <li key={genre.genre_id}>
                            {genre.genre_name}
                        </li>
                    )) : "No genres found."}
                </Typography>
                <Typography variant="body1">
                    Available Platform:
                    {platforms.length > 0 ? platforms.map(platform => (
                        <li key={platform.platform_id}>
                            {platform.platform_name}
                        </li>
                    )) : "No platforms found."}
                </Typography>
            </CardContent>
        </Card>
    </div>;
}

export default Popup;
