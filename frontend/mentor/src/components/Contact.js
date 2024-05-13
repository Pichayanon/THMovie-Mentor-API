import NavBar from "./NavBar";
import CardMedia from '@mui/material/CardMedia';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function Contact() {

    return(
        <div>
            <NavBar />
            <Card sx={{ minWidth: 275 }} style={{margin: 30}}>
                <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                    Contact to our developers
                </Typography>
                <br/>
                <Typography variant="h6" color="text.primary">
                    Devs:
                </Typography>
                <Typography variant="body1">
                    Kongkawee Chayarat : 6510545250
                </Typography>
                <Typography variant="body1">
                    Pichayanon Toojinda : 6510545624
                </Typography>
                <br/>
                <Typography variant="h6" color="text.primary">
                    Github of the project:
                </Typography>
                <br/>
                <a href="https://github.com/Pichayanon/THMovie-Mentor-API">THMovie-Mentor</a>
            </CardContent>
            </Card>
        </div>
    );
}

export default Contact;