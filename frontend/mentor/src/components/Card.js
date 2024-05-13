import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import CardMedia from '@mui/material/CardMedia';
import './Card.css'


export default function BasicCard(props) {
    const { movie, onClick } = props;
    return (
        <Card sx={{ minWidth: 275 }} className='card'>
            {/* <CardMedia
                component="img"
                alt="green iguana"
                height="140"
                image="./images/anya-forger-heh copy 2.avif"
            /> */}
            <CardContent onClick={() => {onClick(movie)}}>
                <Typography gutterBottom variant="h5" component="div">
                    {movie.title_en}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    {movie.title_th}
                </Typography>
            </CardContent>
        </Card>
    );
}