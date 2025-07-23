from urllib import request , parse , error

import requests #diffrent library



url = request.urlopen('https://www.youtube.com/')
urls = 'https://www.youtube.com/'
response = requests.get(url=urls)


# for line in url:
#     print(line.decode().strip())

print(response.request.headers)