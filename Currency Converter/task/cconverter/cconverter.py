import requests, json

from_code = input().lower()

rates_obj = requests.get(f"http://www.floatrates.com/daily/{from_code}.json")
rates_dict = json.loads(rates_obj.text)
rates_cache = {}

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
        print("Checking the cache...")
        if to_code in rates_cache.keys():
            print("Oh! It is in the cache!")
            new_money = round(deposit * rates_cache[to_code], 2)
            print(f"You received {new_money} {to_code.upper()}.")
        else:
            print("Sorry, but it is not in the cache!")
            rates_cache[to_code] = rates_dict[to_code]["rate"]
            new_money = round(deposit * rates_cache[to_code], 2)
            print(f"You received {new_money} {to_code.upper()}.")
    else:
        flag = False
