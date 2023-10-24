import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

# Ask the user for name, remove whitespace from str an capitalize user's name 
name = input("What's your name? ").strip().title()

#Greet user using their name

print(f"Hello, {name}")


### Use docstrings to comment out stuff you dont want python to run!###


