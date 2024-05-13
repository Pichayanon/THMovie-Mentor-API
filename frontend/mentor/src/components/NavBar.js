import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import MenuIcon from '@mui/icons-material/Menu';
import { MenuItem } from '@mui/material';
import Menu from '@mui/material/Menu';
import { createTheme } from '@mui/material/styles';
import * as color from '@mui/material/colors';
import { Link } from 'react-router-dom'
import './NavBar.css'


const theme = createTheme({
    palette: {
      primary: color.red
    },
  });

function NavBar() {
    const [anchorElNav, setAnchorElNav] = React.useState(null);

    const handleOpenNavMenu = (event) => {
        setAnchorElNav(event.currentTarget);
    };

    const handleCloseNavMenu = () => {
        setAnchorElNav(null);
    };


    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static" theme={theme}>
                <Toolbar>
                    <IconButton
                        size="large"
                        aria-label="account of current user"
                        aria-controls="menu-appbar"
                        aria-haspopup="true"
                        onClick={handleOpenNavMenu}
                        color="inherit"
                    >
                        <MenuIcon />
                    </IconButton>
                    <Menu
                        id="menu-appbar"
                        anchorEl={anchorElNav}
                        anchorOrigin={{
                            vertical: 'bottom',
                            horizontal: 'left',
                        }}
                        keepMounted
                        transformOrigin={{
                            vertical: 'top',
                            horizontal: 'left',
                        }}
                        open={Boolean(anchorElNav)}
                        onClose={handleCloseNavMenu}
                    >
                        <MenuItem onClick={handleCloseNavMenu}>
                            <Link to="/about" className='aboutlink'><Typography textAlign="center">About</Typography></Link>
                        </MenuItem>
                        <MenuItem onClick={handleCloseNavMenu}>
                            <Link to="/contact" className='contactlink'><Typography textAlign="center">Contact</Typography></Link>
                        </MenuItem>
                    </Menu>
                    <Typography
                        variant="h6"
                        noWrap
                        component="div"
                        sx={{ flexGrow: 1, display: { xs: 'none', sm: 'block' } }}
                    >
                        MENTOR
                    </Typography>
                    <Link to="/" className='homelink'><Typography textAlign="center">Home</Typography></Link>
                    <Link to="/genre" className='genrelink'><Typography textAlign="center">Search by Genre</Typography></Link>
                    <Link to="/age" className='agelink'><Typography textAlign="center">Search by Age</Typography></Link>
                    <Link to="/visualization" className='visuallink'><Typography textAlign="center">Visualize</Typography></Link>
                </Toolbar>
            </AppBar>
        </Box>
    );
}

export default NavBar;