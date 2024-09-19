import requests

def get_gold_price(api_key):
    url = 'https://api.metalpriceapi.com/v1/latest'
    params = {'api_key': api_key, 'base': 'USD', 'currencies': 'XAU'}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        gold_price = data.get('rates', {}).get('XAU', {}).get('rate')
        return gold_price
    else:
        # Handle API request error
        return None
