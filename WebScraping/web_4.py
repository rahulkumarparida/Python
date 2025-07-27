#pip install bs4 , lxml
import requests
from bs4 import BeautifulSoup
import csv

def Extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response , 'lxml')
    tag = soup.find('div' , { 'id' : 'mp-right' })
    h = tag.find_all('h2')
    content = [i.text for i in h]
    print("tag"  , ' \n ', content)

    with open('wiki.csv' , 'w') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_file.writelines(content  )

Extract(url = "https://en.wikipedia.org/wiki/Main_Page")