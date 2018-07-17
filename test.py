html = '<a target="_blank" title="Python开发工程师（15-30k）' \
       '" href="https://jobs.51job.com/hangzhou-yhq/99817242.html?s=01&t=0" ' \
       'onmousedown>…</a>'
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
tag = soup.a
url = tag.get('href')
print(url)