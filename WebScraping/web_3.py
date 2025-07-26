import requests

url = 'http://127.0.0.1:8000/blog/api/post/'

payload = {
    'title':"pyload",
    'description':"loading this request usong request from my python file",
    'author':1
}

reponse = requests.post(url=url , data=payload)

print(reponse.text)