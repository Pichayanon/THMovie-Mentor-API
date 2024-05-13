import React, { useState, useEffect } from 'react';
import './Visualization.css';
import NavBar from './NavBar';
import { Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import Visualize1 from './Visualize1';
import Visualize2 from './Visualize2';
import Visualize3 from './Visualize3';
import Visualize4 from './Visualize4';

function Visualization() {
    const genres = [
        { id: 'g001', name: 'Action' },
        { id: 'g002', name: 'Comedy' },
        { id: 'g003', name: 'Drama' },
        { id: 'g004', name: 'Romance' },
        { id: 'g005', name: 'Adventure' },
        { id: 'g006', name: 'Crime' },
        { id: 'g007', name: 'Fantasy' },
        { id: 'g008', name: 'History' },
        { id: 'g009', name: 'Horror' },
        { id: 'g010', name: 'Mystery' },
        { id: 'g011', name: 'Sci-Fi' },
        { id: 'g012', name: 'Thriller' },
        { id: 'g013', name: 'Other' },
    ];

    return (
        <div className="app">
            <NavBar/>
            <div className="visualization-grid">
                <div><Visualize1 genres={genres}/></div>
                <div><Visualize2 /></div>
                <div><Visualize3 /></div>
                <div><Visualize4 /></div>
            </div>
        </div>
    );
}

export default Visualization;
