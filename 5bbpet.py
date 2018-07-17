import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.bbpet.top/')
html = html.content.decode('utf-8')
bsobj = BeautifulSoup(html, 'lxml')
for i in bsobj.findAll('div', {'id': 'bt1'}):
    print(i.h2.text)
for j in bsobj.findAll('div', {'id': 'bt2'}):
    print(j.h2.text)