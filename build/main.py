import logging
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from binance import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("trading_bot.log"),
                        logging.StreamHandler()
                    ])


app = Flask(__name__)
CORS(app)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        if not api_key or not api_secret:
            raise ValueError("API key and secret are required.")
        
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        
        try:
            if self.testnet:
                
                self.client = Client(api_key, api_secret, tld='com', testnet=True)
                self.client.FUTURES_URL = 'https://testnet.binancefuture.com'
                self.client.API_URL = 'https://testnet.binancefuture.com' 
            else:
                self.client = Client(api_key, api_secret)

            
            self.client.futures_account()
            logging.info("Binance Futures Testnet client initialized successfully.")
            
        except BinanceAPIException as e:
            logging.error(f"Failed to initialize Binance client: {e}")
            raise ValueError(f"Authentication failed. Please check your API credentials. Error: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred during client initialization: {e}")
            raise ConnectionError(f"Could not connect to Binance. Error: {e}")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            order_params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity
            }
            logging.info(f"Placing {side} {order_type} order for {quantity} {symbol}...")

            if order_type == Client.ORDER_TYPE_LIMIT:
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                order_params['price'] = price
                order_params['timeInForce'] = Client.TIME_IN_FORCE_GTC

            order = self.client.futures_create_order(**order_params)
            logging.info(f"Successfully placed order: {order}")
            return order

        except (BinanceAPIException, BinanceOrderException) as e:
            logging.error(f"Binance Error while placing order: {e}")
            raise e
        except Exception as e:
            logging.error(f"An unexpected error occurred while placing order: {e}")
            raise e


@app.route('/place_order', methods=['POST'])
def place_order_endpoint():
    data = request.get_json()
    logging.info(f"Received request on /place_order: {data}")

    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    if api_key:
        logging.info(f"Verifying API Key loaded from .env: {api_key[:5]}...{api_key[-5:]}")
    else:
        logging.error("API Key was NOT found in environment. Check your .env file.")
    
    if not api_key or not api_secret:
        return jsonify({'status': 'error', 'message': 'Server configuration error: API keys are not set.'}), 500

    if not all(field in data for field in ['symbol', 'side', 'order_type', 'quantity']):
        return jsonify({'status': 'error', 'message': 'Missing required fields.'}), 400

    try:
        bot = BasicBot(api_key=api_key, api_secret=api_secret, testnet=True)
        order_response = bot.place_order(
            symbol=data['symbol'].upper(),
            side=data['side'].upper(),
            order_type=data['order_type'].upper(),
            quantity=float(data['quantity']),
            price=float(data.get('price')) if data.get('price') else None
        )
        return jsonify({'status': 'success', 'data': order_response}), 200

    except (ValueError, ConnectionError) as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    except (BinanceAPIException, BinanceOrderException) as e:
        return jsonify({'status': 'error', 'message': f'Binance Error: {e.message}'}), 500
    except Exception as e:
        logging.error(f"A server error occurred: {e}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'An unexpected server error occurred.'}), 500

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
