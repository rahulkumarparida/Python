import requests 

url = 'https://www.youtube.com/'

response = requests.get(url = url)

print(type(response.text))