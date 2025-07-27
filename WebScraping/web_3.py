import requests

url = 'http://127.0.0.1:8000/blog/api/post/'

payload = {
    'title':"payload",
    'description':"loading this request usong request from my python file",
    'author':1
}

# reponse = requests.post(url=url , data=payload)

params = {
    'offset':'6',
}
reponse = requests.get(url=url , params=params)

print(reponse.text)