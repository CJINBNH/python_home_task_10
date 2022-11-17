import requests

res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

print(res['Valute']["USD"]['Name'], res['Valute']["USD"]['Value'])