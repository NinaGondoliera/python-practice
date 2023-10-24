import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))



print ("Hello world")

### Use docstrings to comment out stuff you dont want python to run!###


