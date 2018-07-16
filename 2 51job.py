import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random


url_dict = {
    '51job爬虫': 'https://search.51job.com/list/080200,000000,0000,00,9,99,%25E7%2588%25AC%25E8%2599%25AB,2,1.html',
    '51job量化': 'https://search.51job.com/list/080200,000000,0000,00,9,99,%25E9%2587%258F%25E5%258C%2596%25E7%25A0%2594%25E7%25A9%25B6%25E5%2591%2598,2,1.html',
    '51job数据分析': 'https://search.51job.com/list/080200,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html',
    '51jobpython': 'https://search.51job.com/list/080200,000000,0000,00,9,99,python,2,1.html',
}
k = random.choice(list(url_dict.keys()))


def get_url():
    i = 1
    url = 'https://search.51job.com/list/080200,000000,0000,00,9,99,python,2,{}.html'.format(i)
    return url


# 请求数据
def get_data(num_retries=3):
    # 关闭多余的连接
    s = requests.session()
    s.keep_alive = False
    url = url_dict[k]
    headers = {'User-Agent':
                    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                    ' Chrome/67.0.3396.99 Safari/537.36'
                }
    try:
        data = requests.get(url, headers=headers, timeout=10)
        print(data.status_code)
    except Exception as e:
        print('链接错误!', e)
        data = None

    if (data != None) and (500 <= data.status_code < 600):
        if (num_retries > 0):
            print('服务器错误,正在重试...')
            time.sleep(1)
            num_retries -= 1
            get_data(num_retries)
    return data


# 解析数据
def parse_data(data):
    soup = BeautifulSoup(data.content, 'lxml')
    jobs = soup.find('div', {'id': 'resultList'})
    jobs = jobs.find_all('div', {'class': 'el'})[1:]

    job_names = []
    job_urls = []
    com_names = []
    work_places = []
    pays = []
    dates = []

    for job in jobs:
        job_name = job.find_all('p', {'class': 't1'})[0].span
        job_name = job_name.text.strip().replace('\n', '')
        job_names.append(job_name)

        job_url = job.find_all('p', {'class': 't1'})[0].span
        job_url = job_url.a.get('href')
        job_urls.append(job_url)

        com_name = job.find_all('span', {'class': 't2'})[0]
        com_name = com_name.a.get('title')
        com_names.append(com_name)

        work_place = job.find_all('span', {'class': 't3'})[0]
        work_place = work_place.get_text()
        work_places.append(work_place)

        pay = job.find_all('span', {'class': 't4'})[0]
        pay = pay.get_text()
        pays.append(pay)

        date = job.find_all('span', {'class': 't5'})[0]
        date = date.get_text()
        dates.append(date)
    return job_names, job_urls, com_names, work_places, pays, dates


# 存储数据
def save_data(job_names, job_urls, com_names, work_places, pays, dates):
    result = pd.DataFrame()
    result['工作岗位'] = job_names
    result['网站'] = job_urls
    result['公司名称'] = com_names
    result['工作地点'] = work_places
    result['工资'] = pays
    result['日期'] = dates

    result.to_csv(k+'.csv', index=None)


# 开始爬取
def run():
    data = get_data()
    job_names, job_urls, com_names, work_places, pays, dates = parse_data(data)
    save_data(job_names, job_urls, com_names, work_places, pays, dates)
    print('数据下载完成!保存到{}!'.format(k+'.csv'))


if __name__ == '__main__':
    run()
