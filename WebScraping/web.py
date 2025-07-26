from urllib import request , parse , error

import requests #diffrent library



url = request.urlopen('https://www.youtube.com/')
# for line in url:
#     print(line.decode().strip())

urls = 'https://images.pexels.com/photos/1324803/pexels-photo-1324803.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'

user = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url=urls , headers=user)


pic = response.content
print('\n')
# print(response.request.headers)
f = open('pexels-photo-1324803.jpeg' , 'wb')
f.write(pic)