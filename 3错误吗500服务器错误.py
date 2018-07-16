import time
import requests

urls = ['http://httpstat.us/500', 'https://www.tumblr.com/',]

'''
服务器错误返回500的状态码,尝试连接3次,每次的等待一秒.
'''


def get_data(url, num_retries=3):
    try:
        # timeout=5表示5秒没反应的话就连接失败
        data = requests.get(url, timeout=5)
        print(data.status_code)
    except requests.exceptions.ConnectionError as e:
        print('错误请求,url:', url)
        print('错误原因:', e)
        data = None
    except:
        print('未知错误,url:', url)
        data = None

    if (data != None) and (500 <= data.status_code < 600):
        if (num_retries > 0):
            print('服务器错误,正在重试...')
            time.sleep(1)
            num_retries -= 1
            get_data(url, num_retries)

    return data


if __name__ == '__main__':
    for url in urls:
        get_data(url)