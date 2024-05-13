import NavBar from "./NavBar";
import CardMedia from '@mui/material/CardMedia';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function About() {

    return(
        <div>
            <NavBar />
            <Card sx={{ minWidth: 275 }} style={{margin: 30}}>
                <CardContent>
                <Typography gutterBottom variant="h4" component="div">
                    What is Mentor?
                </Typography>
                <Typography variant="h6" color="text.secondary">
                    Mentor is a database service for exploring the popular Thai movies and series.

                    The data we have collected are from the response of the our target group via questionaire.
                </Typography>
            </CardContent>
            </Card>
        </div>
    );
}

export default About;