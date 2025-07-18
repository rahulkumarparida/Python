from urllib import request , parse , error

import requests #diffrent library



url = request.urlopen('https://all-student-manger.onrender.com/')
urls = 'https://all-student-manger.onrender.com/'
response = requests.get(url=urls)


# for line in url:
#     print(line.decode().strip())

print(response.request.headers)