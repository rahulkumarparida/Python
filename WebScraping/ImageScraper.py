import requests
import re
import os

imageName = input('Enter the Name of the image: \n')

User_agent = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

url = f"https://www.google.com/search?sca_esv=cb1a46fce0fc5f23&sxsrf=AE3TifPaOLdURi9hUaAshDgi74WpD9APNg:1753619774971&q={imageName}&udm=2"

response = requests.get(url=url, headers=User_agent).text

pattern = r'\["(https://[^"]+\.jpg)",\d+,\d+\]'
images = re.findall(pattern, response)

if images:
    folder_path = f'images/{imageName}'
    os.makedirs(folder_path, exist_ok=True)

    for i, img_url in enumerate(images):
        print(f"Downloading: {img_url}")
        try:
            res = requests.get(img_url, headers=User_agent, timeout=10).content
            with open(f'{folder_path}/{i}.jpg', 'wb') as f:
                f.write(res)
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
else:
    print('No Free Image exists')