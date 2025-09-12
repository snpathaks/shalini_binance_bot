Simplified Binance Futures Trading Bot
A simple yet functional trading bot that allows users to place Market and Limit orders on the Binance Futures Testnet (USDT-M) through a clean, web-based user interface.



✨ Features
Intuitive Web UI: Place trades easily without touching the command line.

Versatile Order Types: Full support for both MARKET and LIMIT orders.

Dual-Sided Trading: Execute BUY (Long) and SELL (Short) positions.

Secure by Design: API keys are managed securely in a .env file, never exposed to the client-side.

Instant Feedback: Receive immediate success or error messages directly from the Binance API.

Robust Logging: All server activity is logged to trading_bot.log for easy debugging.

🛠️ Technology Stack
Backend: Python, Flask

Frontend: HTML, Tailwind CSS, JavaScript

API Wrapper: python-binance

Environment Management: python-dotenv

🚀 Getting Started
Follow these steps to get the trading bot running on your local machine.

Prerequisites
Python 3.7+

A modern web browser (Chrome, Firefox, etc.)

1. Get Binance Futures Testnet API Keys
Important: This bot is designed for the Futures Testnet only. API keys from the main binance.com site will not work.

Navigate to the Binance Futures Testnet website and register or log in.

Go to the API Management section.

Create a new API key.

Ensure the default "Enable Reading" permission is checked.

For IP restrictions, it is recommended to start with "Unrestricted" for testing.

Carefully copy the API Key and Secret Key.

2. Set Up the Backend
Clone the Repository (Optional):
If you have Git, you can clone the repository. Otherwise, just make sure all the project files are in one folder.

git clone <repository-url>
cd <repository-folder>

Create and Activate a Virtual Environment:
It is highly recommended to use a virtual environment to manage project dependencies.

# Create the environment
python -m venv venv

# Activate the environment
# Windows (PowerShell):
.\venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

Install Dependencies:
With the virtual environment active, install the required Python packages:

pip install -r requirements.txt

Create the Environment File:

In the root of the project, create a new file named .env.

Open it and add your API keys from Step 1:

BINANCE_API_KEY="YOUR_TESTNET_API_KEY_HERE"
BINANCE_API_SECRET="YOUR_TESTNET_SECRET_KEY_HERE"

🖥️ How to Run
The application has two parts: the backend server and the frontend UI. Both must be running.

1. Start the Backend Server
Make sure your virtual environment is activated (your terminal prompt should start with (venv)).

Run the Flask server:

python main.py

Keep this terminal window open. The server is now running and listening for requests on http://127.0.0.1:5000.

2. Launch the Frontend
Navigate to the project folder in your computer's File Explorer.

Double-click the index.html file.

This will open the user interface in your default web browser.

📈 Usage
With the index.html page open, fill out the trading form.

Enter the desired Symbol, Order Type, Side, and Quantity.

If you select "Limit", the Price field will appear and must also be filled in.

Click "Place Order".

The result from the Binance API will be displayed at the bottom of the form.

❓ Troubleshooting
ModuleNotFoundError: This means you have not activated your virtual environment. Stop the server (Ctrl+C), run .\venv\Scripts\activate (or source venv/bin/activate), and then run python main.py again.

Authentication failed Error: This error comes directly from Binance. It means your API Key or Secret Key is incorrect, or you generated them on the wrong website (e.g., the main Spot site instead of the Futures Testnet). Double-check your .env file and the source of your keys.

Could not connect to the backend server Error: This means the frontend cannot find your Python server. Make sure the terminal running python main.py is still open and did not crash.

📄 License
This project is licensed under the MIT License.
