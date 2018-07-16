'''
https://miaosha.jd.com/
采集动态生成的ajax
'''

import re, json, requests
from fake_useragent import UserAgent
import pandas as pd


def get_url():
    url_list = ['https://ai.jd.com/index_new?app=Seckill&action=pcMiaoShaAreaList&'
                'callback=pcMiaoShaAreaList&_=1531725911222',
                'https://ai.jd.com/index_new?app=Seckill&action=pcMiaoShaAreaList&'
                'callback=pcMiaoShaAreaList&gid=42&_=1531725969921',
                'https://ai.jd.com/index_new?app=Seckill&action=pcMiaoShaAreaList&'
                'callback=pcMiaoShaAreaList&gid=29&_=1531726015177',
                'https://ai.jd.com/index_new?app=Seckill&action=pcMiaoShaAreaList&'
                'callback=pcMiaoShaAreaList&gid=42&_=1531726020249'
                ]
    return url_list


# 设置json打印的格式 ,indent = 4是缩进
def print_json(data):
    json_str = json.dumps(data, indent=4, ensure_ascii=False)
    print(json_str)


def get_data(json_url):
    p_names = []
    p_prices = []
    p_rates = []
    p_times = []
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    data = requests.get(json_url, headers=headers)
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


def save_data(p_names, p_prices, p_rates, p_times):
    result = pd.DataFrame()
    result['秒杀商品'] = p_names
    result['价格'] = p_prices
    result['折扣'] = p_rates
    result['开始时间'] = p_times
    result.to_csv('2京东秒杀.csv', index=None)


if __name__ == '__main__':
    p_names_f = []
    p_prices_f = []
    p_rates_f = []
    p_times_f = []
    url_list = get_url()
    for json_url in url_list:
        p_names, p_prices, p_rates, p_times = get_data(json_url)
        p_names_f += p_names
        p_prices_f += p_prices
        p_rates_f += p_rates
        p_times_f += p_times
    save_data(p_names_f, p_prices_f, p_rates_f, p_times_f)


