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
                    Here are contact to our devs.
                </Typography>
                <Typography variant="body1" color="text.secondary">
                    Kongkawee Chayarat : 6510545250
                </Typography>
                <Typography variant="body1" color="text.secondary">
                    Pichayanon Toojinda : 6510545624
                </Typography>
            </CardContent>
            </Card>
        </div>
    );
}

export default Contact;