from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from configparser import ConfigParser
  
configur = ConfigParser()
configur.read('alpaca.ini')

key = configur.get('bearishbets','API_KEY')
secret = configur.get('bearishbets','API_SECRET')

trading_client = TradingClient(key, secret, paper=True)

# preparing market order
market_order_data = MarketOrderRequest(
                    symbol="TSLA",
                    qty=100,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )

