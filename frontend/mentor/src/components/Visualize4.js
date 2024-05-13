import React, { useState, useEffect } from 'react';
import { Pie } from 'react-chartjs-2';
import './Visualization.css';

function Visualize4() {
    const [movieData, setMovieData] = useState([]);

    useEffect(() => {
        const fetchMovieData = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/TH-Movies/movies/');
                if (!response.ok) {
                    throw new Error('Failed to fetch data');
                }
                const movies = await response.json();
                const tvSeriesCount = movies.filter(movie => movie.type === 'tv-series').length;
                const movieCount = movies.length - tvSeriesCount;
                setMovieData([
                    { type: 'TV Series', count: tvSeriesCount },
                    { type: 'Movie', count: movieCount }
                ]);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchMovieData();
    }, []);

    // Calculate total count
    const totalCount = movieData.reduce((acc, curr) => acc + curr.count, 0);

    // Prepare chart data
    const chartData = {
        labels: movieData.map(item => item.type),
        datasets: [{
            data: movieData.map(item => (item.count / totalCount) * 100),
            backgroundColor: ['#FF6384', '#36A2EB'], // Red for TV Series, Blue for Movies
            hoverBackgroundColor: ['#FF6384', '#36A2EB']
        }]
    };

    return (
        <div className="visualization-block">
            <div className='title'>
                <h1>Percentage of Movie Types</h1>
            </div>
            <div className='charter'>
                {movieData.length > 0 ? (
                    <Pie data={chartData} />
                ) : (
                    <svg className='loading' viewBox="25 25 50 50">
                        <circle r="20" cy="50" cx="50"></circle>
                    </svg>
                )}
            </div>
        </div>
    );
}

export default Visualize4;