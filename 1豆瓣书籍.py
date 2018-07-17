import requests
from bs4 import BeautifulSoup
import pandas as pd


# 请求数据
def get_data():
    http = 'https://book.douban.com/'
    headers = {'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/67.0.3396.99 Safari/537.36'
}
    data = requests.get(http, headers=headers)
    # print(data.text)
    return data


# 解析数据
def parse_data(data):
    soup = BeautifulSoup(data.text, 'lxml')
    # print(soup)

    book_xia = soup.find('ul', {'class': 'list-col list-col2 list-summary s'})
    book_xia = book_xia.find_all('li')

    img_urls = []
    titles = []
    ratings = []
    authors = []
    details = []

    for book in book_xia:
        # 封面图片url
        img_url = book.find_all('a')[0].find('img').get('src')
        img_urls.append(img_url)


        # 图书标题
        title = book.find_all('a')[1].get_text()
        titles.append(title)



        # 评价星级
        rating = book.find('p', {'class': 'reviews'}).get_text()
        tating = rating.replace('\n', '').strip()
        ratings.append(tating)


        # 作者及出版信息
        author = book.find('p', {'class': 'author'}).get_text()
        author = author.replace('\n', '').replace(' ', '')
        authors.append(author)


        # 图书简介
        detail = book.find('p', {'class': 'book-list-classification'}).get_text()
        detail = detail.replace('\n', '').replace(' ', '')
        details.append(detail)


        print('img_urls', img_urls)
        print('titles', titles)
        print('ratings', ratings)
        print('authors', authors)
        print('details', details)
    return img_urls, titles, ratings, authors, details


# 存储数据
def save_data(img_urls, titles, ratings, authors, details):
    # 创建空的DataFrame数据框
    result = pd.DataFrame()
    result['img_urls'] = img_urls
    result['titles'] = titles
    result['ratings'] = ratings
    result['authors'] = authors
    result['details'] = details
    result.to_csv('1豆瓣书籍.csv', index=None)


# 开始爬取
def run():
    data = get_data()
    img_urls, titles, ratings, authors, details = parse_data(data)
    save_data(img_urls, titles, ratings, authors, details)


if __name__ == '__main__':
    run()