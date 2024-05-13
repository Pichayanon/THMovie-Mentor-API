import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import './Visualization.css';

function Visualize3() {
    const platforms = [
        { id: 'p001', name: 'prime_video' },
        { id: 'p002', name: 'apple_tv' },
        { id: 'p003', name: 'netflix' },
        { id: 'p004', name: 'viu' },
        { id: 'p005', name: 'youtube' },  // corrected spelling from "youyube" to "youtube"
        { id: 'p006', name: '3ch_plus' }
    ];

    const [platformData, setPlatformData] = useState([]);

    useEffect(() => {
        const fetchPlatformData = async () => {
            const dataPromises = platforms.map(platform =>
                fetch(`http://127.0.0.1:8000/TH-Movies/movies/platform/${platform.id}`)
                    .then(response => response.json())
                    .then(movies => ({ name: platform.name, count: movies.length }))
            );

            const results = await Promise.all(dataPromises);
            setPlatformData(results);
        };

        fetchPlatformData();
    }, []);

    // Prepare chart data
    const chartData = {
        labels: platformData.map(p => p.name),
        datasets: [{
            label: 'Number of Movies by Platform',
            data: platformData.map(p => p.count),
            backgroundColor: 'rgba(153, 102, 255, 0.5)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1,
        }]
    };

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
            <div className='title'>
                <h1>Movie Availability by Platform</h1>
            </div>
            <div className='visualizer'>
                {platformData.length > 0 ? (
                    <Bar data={chartData} options={options} />
                ) : (
                    <svg className='loading' viewBox="25 25 50 50">
                        <circle r="20" cy="50" cx="50"></circle>
                    </svg>
                )}
            </div>
        </div>
    );
}

export default Visualize3;
