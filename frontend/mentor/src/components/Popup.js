import { useEffect, useState } from "react";
import './Popup.css';
import CardMedia from '@mui/material/CardMedia';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';


function Popup(props) {
    const {movie, onPopupClose} = props;
    const [movieData, setMovieData] = useState([]);
    const [actors, setActors] = useState([]);
    const [genres, setGenres] = useState([]);
    const [platforms, setPlatforms] = useState([]);

    useEffect(() => {
        document.documentElement.style.overflowY = 'hidden';
        return () => {
            document.documentElement.style.overflowY = 'auto';
        }
    }, []);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/TH-Movies/movies/${movie}`).then(res => {
            return res.json();
        }).then(resJson => {
            setMovieData(resJson);
            setActors(resJson.actors);
            setGenres(resJson.genres);
            setPlatforms(resJson.platforms);
        });
    }, [movie]);

    return <div className="popup" onClick={onPopupClose}>
        <Card sx={{ minWidth: 275 }} style={{margin: 80}}>
            {/* <CardMedia
                component="img"
                alt="green iguana"
                height="300"
                image="./images/anya-forger-heh copy 2.avif"
            /> */}
            <CardContent>
                <Typography gutterBottom variant="h4" component="div">
                    {movieData.title_en}
                </Typography>
                <Typography variant="h6" color="text.secondary">
                    {movieData.title_th} - {movieData.release_year}
                </Typography>
                <Typography variant="body1">
                    Top Actors:
                    {actors.map(actor => (
                        <li key={actor.actor_id}>
                            {actor.fullname_en} ({actor.nickname_en})
                        </li>
                    ))}
                </Typography>
                <Typography variant="body1">
                    Genres:
                    {genres.map(genre => (
                        <li key={genre.genre_id}>
                            {genre.genre_name}
                        </li>
                    ))}
                </Typography>
                <Typography variant="body1">
                    Available Platform:
                    {platforms.map(platform => (
                        <li key={platform.platform_id}>
                            {platform.platform_name}
                        </li>
                    ))}
                </Typography>
            </CardContent>
        </Card>
    </div>;
}

export default Popup;