import requests
print('Start api read application')


paginaresults = requests.get('https://catfact.ninja/facts')
print(paginaresults)

feitjes = paginaresults.json()
print(feitjes["current_page"])
print(feitjes["data"][1]["fact"])
