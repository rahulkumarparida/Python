import requests
import re
import os

imageName = input('Enter the Name of the image : \n')


response = requests.get(url=url , headers=User_agent).text

pattern = r'\["https://[^"]+\.jpg",[0-9]+,[0-9]+\]'
images = re.findall(pattern , response) 

os.makedirs('images', exist_ok=True)

for i, img in enumerate(images):
    
    url_pattern = r'"(https://[^"]+\.jpg)"'
    imgurl = re.findall(url_pattern , img)
    
    if imgurl:
        print(f"Downloading: {imgurl[0]}")
        res = requests.get(imgurl[0]).content

        with open(f'images/{i}.jpg', 'wb') as f:
            f.write(res)


#\x01\x92?\xba;


#["https://nomoneynotime.com.au/imager/uploads/articles/17715/shutterstock_1919291432_374635aacd4cafccef5bb0653ee5dedb.jpeg",675,900]