import requests
from random import choice
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format('Random Jokes')
header = colored(header, color='green')
print(header)
user_input = input('What would you like to search for? ')
url = 'https://icanhazdadjoke.com/search'
res = requests.get(url,
                   headers={'accept': 'application/json'},
                   params={'term': user_input}
                   ).json()

# print(res['results'])
result = res['results']
# print(len(result))
num_jokes = res['total_jokes']
if num_jokes > 1:
    print(f'''I found {num_jokes} jokes about {user_input}, Here's one: ''')
    print(choice(result)['joke'])
elif num_jokes == 1:
    print('There is one joke')
    print(choice(result)['joke'])
else:
    print(f'There are no jokes with {user_input} in it')
