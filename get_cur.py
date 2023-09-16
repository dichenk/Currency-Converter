import requests

the_really_secret_key = '3989fcdb6dd04ef8adf1536619f0f685'


def get_the_currency(from_cur='USD', to_cur='RUB'):
    
    data = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={the_really_secret_key}&base={from_cur}&symbols={to_cur}').json()
    return data['rates'][to_cur]

