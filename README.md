# tradingbot
Simplified Binance Futures Trading Bot
This project is a simple yet functional trading bot that allows users to place Market and Limit orders on the Binance Futures Testnet (USDT-M) through a clean, web-based user interface.

The application consists of a Python backend powered by Flask and a lightweight HTML, CSS, and JavaScript frontend.

Features
Web-Based UI: An intuitive interface to place trades without using the command line.

Order Types: Supports both MARKET and LIMIT orders.

Order Sides: Supports both BUY (Long) and SELL (Short) positions.

Secure Credentials: API keys and secrets are managed securely using an .env file and are never exposed to the frontend.

Real-time Feedback: The UI provides immediate success or error messages from the Binance API.

Logging: All server requests, API responses, and errors are logged to trading_bot.log for easy debugging.

Project Structure
/
├── .env                  # Stores secret API keys (must be created manually)
├── .gitignore            # Specifies files for Git to ignore
├── index.html            # Frontend HTML structure
├── style.css             # Frontend styling
├── script.js             # Frontend JavaScript logic
├── main.py               # Backend Flask server
├── requirements.txt      # Python dependencies
└── trading_bot.log       # Log file (auto-generated)

Setup and Installation
Follow these steps to get the trading bot running on your local machine.

1. Prerequisites
Python 3.7+

A web browser

2. Get Binance Futures Testnet API Keys
Go to the Binance Futures Testnet website and register or log in.

Navigate to the API Management section.

Create a new API key. Ensure the default "Enable Reading" permission is checked. You do not need to enable any other permissions for this bot.

Copy the API Key and Secret Key. You will need them in a later step.

3. Set Up the Backend
Create a Virtual Environment:
Open a terminal in the project directory and run:

python -m venv venv

Activate the Environment:

Windows (PowerShell): .\venv\Scripts\activate

macOS / Linux: source venv/bin/activate

Install Dependencies:
With the virtual environment active, install the required Python packages:

pip install -r requirements.txt

Create the Environment File:

Create a new file in the root of the project named .env.

Open the .env file and add your API keys in the following format:

BINANCE_API_KEY="YOUR_TESTNET_API_KEY_HERE"
BINANCE_API_SECRET="YOUR_TESTNET_SECRET_KEY_HERE"

How to Run the Application
The application has two parts that must be running at the same time: the backend server and the frontend UI.

1. Start the Backend Server
Make sure your virtual environment is activated.

Run the Flask server from your terminal:

python main.py

Keep this terminal window open. You should see output indicating the server is running on http://127.0.0.1:5000.

2. Launch the Frontend
Navigate to the project folder in your computer's File Explorer.

Double-click the index.html file to open it in your web browser.

Usage
With the index.html page open, fill out the trading form.

Enter the desired Symbol, Order Type, Side, and Quantity.

If you select "Limit" as the order type, the Price field will appear and must be filled in.

Click "Place Order".

The result from the Binance API will be displayed at the bottom of the form.
