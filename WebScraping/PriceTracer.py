import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/maan-men-slippers/p/itmaa6067e699f14?pid=SFFH3XNTESMM9HEU&lid=LSTSFFH3XNTESMM9HEUBNIGVD&marketplace=FLIPKART&store=osp%2Fcil%2Fe1r&srno=b_1_3&otracker=browse&fm=organic&iid=608b4834-b5f5-4c2a-ba8b-3a5aa5af6fc6.SFFH3XNTESMM9HEU.SEARCH&ppt=browse&ppn=browse&ssid=ephg07riq80000001753786948370'


class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.User_agent = {'User_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}
        self.response = requests.get(url=self.url , headers=self.User_agent).text
        
        self.soup = BeautifulSoup(self.response , 'lxml')
       


    def product_name(self):
        title = self.soup.find('span' , {'class': 'VU-ZEz'})
        if title is not None:
            return title.text
        else:
            return 'Tag Not Found'
    def product_price(self):
        price = self.soup.find('div' , {'class': 'Nx9bqj CxhGGd'})
        
        if price is not None:
            return price.text
        else:
            return 'Tag Not Found'

        






device = PriceTracer(url=url)

print(device.product_name())
print(device.product_price())

