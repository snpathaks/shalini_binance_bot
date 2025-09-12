<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Infographic: The Anatomy of a Simplified Trading Bot</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0F172A;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 350px;
            }
        }
        .flow-card {
            background-color: #1E293B;
            border: 1px solid #334155;
            min-height: 120px;
        }
        .flow-arrow {
            color: #9B5DE5;
            font-size: 2.5rem;
            line-height: 1;
        }
    </style>
</head>
<body class="text-gray-200">

    <div class="container mx-auto p-4 md:p-8 max-w-7xl">

        <header class="text-center my-12">
            <h1 class="text-5xl md:text-6xl font-extrabold text-white leading-tight">The Anatomy of a <span style="color: #00F5D4;">Trading Bot</span></h1>
            <p class="mt-4 text-lg md:text-xl text-slate-400 max-w-3xl mx-auto">A visual deep-dive into the architecture, functionality, and simulated performance of the Simplified Binance Futures Trading Application.</p>
        </header>

        <main class="space-y-16">
            
            <section id="architecture">
                <div class="text-center mb-10">
                    <h2 class="text-4xl font-bold text-white">Application Architecture</h2>
                    <p class="mt-2 text-slate-400 max-w-2xl mx-auto">Visualizing the journey of a trade from a user's click to its execution on the Binance exchange, highlighting the secure and decoupled design.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-5 items-center gap-4 text-center">
                    <div class="flow-card rounded-lg p-4 flex flex-col justify-center items-center">
                        <span class="text-5xl mb-2">👤</span>
                        <h3 class="font-bold text-lg text-white">User Interface</h3>
                        <p class="text-sm text-slate-400">Frontend built with HTML, Tailwind CSS, & JS</p>
                    </div>
                    
                    <div class="flow-arrow transform md:rotate-0 rotate-90">→</div>

                    <div class="flow-card rounded-lg p-4 flex flex-col justify-center items-center">
                        <span class="text-5xl mb-2">⚙️</span>
                        <h3 class="font-bold text-lg text-white">Backend Server</h3>
                        <p class="text-sm text-slate-400">Python & Flask API handles logic and security</p>
                    </div>

                    <div class="flow-arrow transform md:rotate-0 rotate-90">→</div>

                    <div class="flow-card rounded-lg p-4 flex flex-col justify-center items-center">
                        <span class="text-5xl mb-2">🔗</span>
                        <h3 class="font-bold text-lg text-white">Binance API</h3>
                        <p class="text-sm text-slate-400">Secure execution via the official exchange API</p>
                    </div>
                </div>
            </section>
            
            <section id="functionality">
                <div class="text-center mb-10">
                    <h2 class="text-4xl font-bold text-white">Core Functionality</h2>
                    <p class="mt-2 text-slate-400 max-w-2xl mx-auto">The bot's primary functions are placing different types of orders. Here’s a breakdown of simulated activity over a 24-hour period.</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-800 rounded-lg shadow-lg p-6">
                        <h3 class="text-xl font-bold text-white mb-2 text-center">Simulated Order Type Distribution</h3>
                        <p class="text-center text-sm text-slate-400 mb-4">Limit orders are used more frequently for precise entry points, while market orders provide immediate execution.</p>
                        <div class="chart-container">
                            <canvas id="orderTypeChart"></canvas>
                        </div>
                    </div>
                    <div class="bg-slate-800 rounded-lg shadow-lg p-6">
                        <h3 class="text-xl font-bold text-white mb-2 text-center">Simulated Trading Volume (USDT)</h3>
                        <p class="text-center text-sm text-slate-400 mb-4">A comparison of the total volume traded for buy (long) versus sell (short) positions across all order types.</p>
                        <div class="chart-container">
                            <canvas id="buySellChart"></canvas>
                        </div>
                    </div>
                </div>
            </section>

            <section id="performance">
                <div class="text-center mb-10">
                    <h2 class="text-4xl font-bold text-white">Simulated Performance Metrics</h2>
                    <p class="mt-2 text-slate-400 max-w-2xl mx-auto">To evaluate the bot's potential, we simulated its performance over a 30-day period, tracking portfolio growth and operational reliability.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div class="md:col-span-2 bg-slate-800 rounded-lg shadow-lg p-6">
                         <h3 class="text-xl font-bold text-white mb-2 text-center">30-Day Simulated Portfolio Growth</h3>
                        <p class="text-center text-sm text-slate-400 mb-4">This chart illustrates the hypothetical growth of a 10,000 USDT portfolio based on the bot's trading strategy.</p>
                        <div class="chart-container" style="height: 350px; max-height: 450px;">
                            <canvas id="portfolioGrowthChart"></canvas>
                        </div>
                    </div>
                    <div class="bg-slate-800 rounded-lg shadow-lg p-6 flex flex-col justify-center">
                        <h3 class="text-xl font-bold text-white mb-2 text-center">API Call Success Rate</h3>
                        <p class="text-center text-sm text-slate-400 mb-4">Measures the reliability of the bot's connection and order placement with the Binance API.</p>
                        <div class="chart-container" style="height: 250px;">
                            <canvas id="successRateChart"></canvas>
                        </div>
                        <div class="text-center mt-4">
                             <p class="text-6xl font-extrabold" style="color: #00F5D4;">99.8%</p>
                             <p class="text-slate-400 font-medium">Successful API Calls</p>
                        </div>
                    </div>
                </div>
            </section>

            <section id="stack">
                <div class="text-center mb-10">
                    <h2 class="text-4xl font-bold text-white">Technology Stack</h2>
                     <p class="mt-2 text-slate-400 max-w-2xl mx-auto">The tools and technologies that power the entire application, from user interface to trade execution.</p>
                </div>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
                    <div class="bg-slate-800 p-6 rounded-lg">
                        <h3 class="font-bold text-xl" style="color: #00CCBF;">Frontend</h3>
                        <ul class="mt-2 text-slate-300">
                            <li>HTML5</li>
                            <li>Tailwind CSS</li>
                            <li>JavaScript</li>
                        </ul>
                    </div>
                     <div class="bg-slate-800 p-6 rounded-lg">
                        <h3 class="font-bold text-xl" style="color: #9B5DE5;">Backend</h3>
                        <ul class="mt-2 text-slate-300">
                            <li>Python 3</li>
                            <li>Flask</li>
                            <li>CORS</li>
                        </ul>
                    </div>
                     <div class="bg-slate-800 p-6 rounded-lg">
                        <h3 class="font-bold text-xl" style="color: #F15BB5;">API & Tooling</h3>
                        <ul class="mt-2 text-slate-300">
                            <li>Binance API</li>
                            <li>python-binance</li>
                            <li>python-dotenv</li>
                        </ul>
                    </div>
                     <div class="bg-slate-800 p-6 rounded-lg">
                        <h3 class="font-bold text-xl" style="color: #FEE440;">Infrastructure</h3>
                        <ul class="mt-2 text-slate-300">
                            <li>Virtual Env (venv)</li>
                            <li>Flask Dev Server</li>
                            <li>Logging</li>
                        </ul>
                    </div>
                </div>
            </section>

        </main>
        
        <footer class="text-center mt-16 py-8 border-t border-slate-700">
            <p class="text-slate-500">Infographic generated based on the "Simplified Binance Futures Trading Bot" project.</p>
        </footer>

    </div>

    <script>
        const energeticPlayfulPalette = {
            cyan: '#00F5D4',
            turquoise: '#00CCBF',
            purple: '#9B5DE5',
            pink: '#F15BB5',
            yellow: '#FEE440',
            slate: 'rgba(100, 116, 139, 0.7)',
            white: 'rgba(255, 255, 255, 0.8)',
        };

        const processLabel = (label) => {
            if (typeof label !== 'string' || label.length <= 16) {
                return label;
            }
            const words = label.split(' ');
            const lines = [];
            let currentLine = '';
            for (const word of words) {
                if ((currentLine + word).length > 16) {
                    lines.push(currentLine.trim());
                    currentLine = '';
                }
                currentLine += word + ' ';
            }
            lines.push(currentLine.trim());
            return lines;
        };

        const multiLineTooltipTitle = {
            plugins: {
                tooltip: {
                    callbacks: {
                        title: function(tooltipItems) {
                            const item = tooltipItems[0];
                            let label = item.chart.data.labels[item.dataIndex];
                            if (Array.isArray(label)) {
                              return label.join(' ');
                            }
                            return label;
                        }
                    }
                }
            }
        };

        const defaultChartOptions = {
            maintainAspectRatio: false,
            responsive: true,
            plugins: multiLineTooltipTitle.plugins,
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { color: 'rgba(255, 255, 255, 0.1)' },
                    ticks: { color: energeticPlayfulPalette.slate }
                },
                x: {
                    grid: { display: false },
                    ticks: { color: energeticPlayfulPalette.slate }
                }
            },
            legend: {
                labels: {
                    color: energeticPlayfulPalette.white
                }
            }
        };
        
        new Chart(document.getElementById('orderTypeChart'), {
            type: 'doughnut',
            data: {
                labels: ['Limit Orders', 'Market Orders'],
                datasets: [{
                    label: 'Order Types',
                    data: [68, 32],
                    backgroundColor: [energeticPlayfulPalette.purple, energeticPlayfulPalette.cyan],
                    borderColor: '#1E293B',
                    borderWidth: 4,
                }]
            },
            options: {
                maintainAspectRatio: false,
                responsive: true,
                plugins: {
                    ...multiLineTooltipTitle.plugins,
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: energeticPlayfulPalette.white,
                            padding: 20,
                            font: { size: 14 }
                        }
                    }
                }
            }
        });

        new Chart(document.getElementById('buySellChart'), {
            type: 'bar',
            data: {
                labels: ['Buy (Long) Volume', 'Sell (Short) Volume'],
                datasets: [{
                    label: 'Volume in USDT',
                    data: [1250350, 980750],
                    backgroundColor: [energeticPlayfulPalette.cyan, energeticPlayfulPalette.pink],
                    borderColor: [energeticPlayfulPalette.cyan, energeticPlayfulPalette.pink],
                    borderWidth: 1,
                    borderRadius: 5,
                }]
            },
            options: { ...defaultChartOptions, plugins: { ...defaultChartOptions.plugins, legend: { display: false } } }
        });

        new Chart(document.getElementById('portfolioGrowthChart'), {
            type: 'line',
            data: {
                labels: ['Day 1', 'Day 5', 'Day 10', 'Day 15', 'Day 20', 'Day 25', 'Day 30'],
                datasets: [{
                    label: 'Portfolio Value (USDT)',
                    data: [10000, 10250, 10800, 10750, 11500, 11900, 12850],
                    fill: true,
                    backgroundColor: 'rgba(0, 245, 212, 0.2)',
                    borderColor: energeticPlayfulPalette.cyan,
                    tension: 0.4,
                    pointBackgroundColor: energeticPlayfulPalette.cyan,
                    pointRadius: 5,
                }]
            },
            options: { ...defaultChartOptions, plugins: { ...defaultChartOptions.plugins, legend: { display: false } } }
        });

        new Chart(document.getElementById('successRateChart'), {
            type: 'doughnut',
            data: {
                labels: ['Successful Calls', 'Failed Calls'],
                datasets: [{
                    label: 'API Calls',
                    data: [998, 2],
                    backgroundColor: [energeticPlayfulPalette.cyan, energeticPlayfulPalette.pink],
                    borderColor: '#1E293B',
                    borderWidth: 4,
                    circumference: 180,
                    rotation: 270,
                }]
            },
            options: {
                maintainAspectRatio: false,
                responsive: true,
                plugins: {
                    ...multiLineTooltipTitle.plugins,
                    legend: { display: false },
                    tooltip: { enabled: false }
                },
                cutout: '70%',
            }
        });
    </script>
</body>
</html>
