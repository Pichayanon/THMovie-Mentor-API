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
                <Typography variant="h5" color="text.primary">
                    Background
                </Typography>
                <Typography>
                    <br/>
                    When we want to watch a Thai movie, it is not easy to find one that suits our age or gender. Current websites do not offer recommenders that truly provide good suggestions. Therefore, we are trying to ask the target group about their favorite movies across various ages and genders.
                </Typography>
                    <br/>
                <Typography variant="h5" color="text.primary">
                    Goals
                </Typography>
                <Typography>
                    <br/>
                    The goal is to offer a versatile API that enables detailed data access and visualization, facilitating trend analysis and content recommendations within the Thai entertainment industry.
                </Typography>
            </CardContent>
            </Card>
        </div>
    );
}

export default About;