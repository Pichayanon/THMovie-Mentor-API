import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import './Visualization.css';

function Visualize2() {
    const [chartData, setChartData] = useState({});

    useEffect(() => {
        const fetchGenreCounts = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/TH-Movies/genres/genderCounts/');
                const data = await response.json();
                const labels = data.map(genre => genre.genre_name);
                const maleData = data.map(genre => genre.gender_counts.male);
                const femaleData = data.map(genre => genre.gender_counts.female);

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
            } catch (error) {
                console.error('Failed to fetch data:', error);
                setChartData({});
            }
        };

        fetchGenreCounts();
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
            <div className='title'>
                <h1>Genre Preferences by Gender</h1>
            </div>
            <div className='visualizer'>
                {chartData.labels ? (
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

export default Visualize2;
