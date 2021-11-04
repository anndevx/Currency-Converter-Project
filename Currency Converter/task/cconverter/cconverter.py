import requests, json

# Take the currency code,
# the amount of money that you have,
# and the currency code that you want to receive as the user input.
from_code = input().lower()

# Retrieve the data from FloatRates as in the previous exercises.
rates_obj = requests.get(f"http://www.floatrates.com/daily/{from_code}.json")
rates_dict = json.loads(rates_obj.text)
rates_cache = {}

# Cache the exchange rates taken from URL
if from_code == 'usd':
    rates_cache['eur'] = rates_dict['eur']['rate']
elif from_code == 'eur':
    rates_cache['usd'] = rates_dict['usd']['rate']
else:
    rates_cache['usd'] = rates_dict['usd']['rate']
    rates_cache['eur'] = rates_dict['eur']['rate']

flag = True
while flag:
    to_code = input().lower()
    if to_code:
        deposit = float(input())

        # Take a look at the cache; maybe you already have what you need?
        print("Checking the cache...")
        if to_code in rates_cache.keys():
            print("Oh! It is in the cache!")
            # calculate exchange
            new_money = round(deposit * rates_cache[to_code], 2)
            print(f"You received {new_money} {to_code.upper()}.")
        else:
            print("Sorry, but it is not in the cache!")
            # get from rates_dict and add to rates_cache
            rates_cache[to_code] = rates_dict[to_code]["rate"]
            # calculate exchange
            new_money = round(deposit * rates_cache[to_code], 2)
            print(f"You received {new_money} {to_code.upper()}.")
    else:
        flag = False
