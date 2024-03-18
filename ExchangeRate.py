import requests
import json

class ExchangeRate:
    # constructor
    def __init__(self):
        self.url = 'http://api-cryptopia.adca.sh/v1/prices/ticker'
        self.exchange_rate = self.get_exchange_rate()

    # Exchange from the api
    def get_exchange_rate(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            # iterating over the data
            for item in data['data']:
                if item['symbol'] == 'BTC/EUR':
                    return float(item['value'])
            print("Warning: The key 'BTC/EUR' was not found in the response.")
            return None  #
        except requests.RequestException as e:
            print(f"Error fetching exchange rate: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing exchange rate data: {e}")
            return None
# Convert btc to euro, it didn't work at first so I put return none if it cant find it, but now it should work.
    def btc_to_eur(self, btc_amount):
        if self.exchange_rate is None:
            return None
        else:
            return btc_amount * self.exchange_rate
