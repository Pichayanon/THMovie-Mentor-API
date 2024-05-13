import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import './Visualization.css';

function Visualize2() {
    const [chartData, setChartData] = useState({});
    const genders = ['Male', 'Female'];

    useEffect(() => {
        const genreCounts = { Male: {}, Female: {} };

        const fetchMoviesAndGenres = async (gender) => {
            const movieResponse = await fetch(`http://127.0.0.1:8000/TH-Movies/movies/gender/${gender}/`);
            const movies = await movieResponse.json();

            for (const movie of movies) {
                const genresResponse = await fetch(`http://127.0.0.1:8000/TH-Movies/genresOfMovie/${movie.movie_id}/`);
                const genres = await genresResponse.json();
                
                genres.forEach(genre => {
                    genreCounts[gender][genre.genre_name] = (genreCounts[gender][genre.genre_name] || 0) + 1;
                });
            }
            return genreCounts;
        };

        Promise.all(genders.map(gender => fetchMoviesAndGenres(gender)))
            .then(() => {
                const labels = Array.from(new Set([...Object.keys(genreCounts.Male), ...Object.keys(genreCounts.Female)]));
                const maleData = labels.map(label => genreCounts.Male[label] || 0);
                const femaleData = labels.map(label => genreCounts.Female[label] || 0);

                setChartData({
                    labels,
                    datasets: [
                        {
                            label: 'Male',
                            data: maleData,
                            backgroundColor: 'rgba(54, 162, 235, 0.5)'
                        },
                        {
                            label: 'Female',
                            data: femaleData,
                            backgroundColor: 'rgba(255, 99, 132, 0.5)'
                        }
                    ]
                });
            });
    }, []);

    const options = {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            legend: {
                position: 'top'
            }
        }
    };

    return (
        <div className="visualization-block">
            <div>
                <h1>Genre Preferences by Gender</h1>
            </div>
            {chartData.labels ? (
                <Bar data={chartData} options={options} />
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}

export default Visualize2;
