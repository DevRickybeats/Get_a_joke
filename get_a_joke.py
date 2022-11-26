import requests
tut = input('What would you like to search for? ')
url = 'https://icanhazdadjoke.com/search'
res = requests.get(url,
                   headers={'accept': 'application/json'},
                   params={'term': tut}
                   ).json()

print(res)
