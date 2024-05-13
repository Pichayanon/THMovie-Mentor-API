import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import './Visualization.css';

function Visualize1(props) {
    const {genres} = props;
    const [genreData, setGenreData] = useState([]);

    useEffect(() => {
        const fetchGenreData = async () => {
            const dataPromises = genres.map(genre =>
                fetch(`http://127.0.0.1:8000/TH-Movies/movies/genre/${genre.id}`)
                    .then(response => response.json())
                    .then(movies => ({ name: genre.name, count: movies.length }))
            );

            const results = await Promise.all(dataPromises);
            setGenreData(results);
        };

        fetchGenreData();
    }, []);

    // Prepare chart data
    const chartData = {
        labels: genreData.map(g => g.name),
        datasets: [{
            label: 'Number of Movies by Genre',
            data: genreData.map(g => g.count),
            backgroundColor: 'rgba(75, 192, 192, 0.5)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
        }]
    };

    const options = {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    };

    return (
        <div className="visualization-block">
            <div>
                <h1>Movie Count by Genre</h1>
            </div>
            {genreData.length > 0 ? (
                <Bar data={chartData} options={options} />
            ) : (
                <p>Loading...</p>
            )}
        </div>
    )
}

export default Visualize1;