import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re, json, requests
from fake_useragent import UserAgent
import pandas as pd


def getdata(data):
    p_names = []
    p_prices = []
    p_rates = []
    p_times = []
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    # print(data.text)

    # pcMiaoShaAreaList 在preview最外层最上面
    re_data = re.findall('pcMiaoShaAreaList\(({.*})\)', data.text)[0]
    json_data = json.loads(re_data)

    miaoShaList = json_data['miaoShaList']
    # print(len(miaoShaList))
    # print(type(miaoShaList))
    # # print_json(miaoShaList)

    for each in miaoShaList:
        p_name = each['wname']
        p_names.append(p_name)

        p_price = each['jdPrice']
        p_prices.append(p_price)

        p_rate = each['rate']
        p_rates.append(p_rate)

        p_time = each['startTimeShow']
        p_times.append(p_time)

    return p_names, p_prices, p_rates, p_times


def run():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    json_url = 'https://miaosha.jd.com/'
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(json_url)
    time.sleep(1)

    html = driver.page_source
    print(html)

    data = getdata(html)

    driver.quit()
    return data


if __name__ == '__main__':
    run()