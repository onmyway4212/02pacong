import re, time, requests, urllib.robotparser
from fake_useragent import UserAgent
import chardet


def get_headers():
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}
    return headers


def get_proxies():
    proxies = {
        'http': '125.88.74.122:84',
        'http': '123.84.13.240:8118',
        'https': '94.240.33.242:3128',
    }
    return proxies


def robot_check(robotstxt_url, headers, url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robotstxt_url)
    rp.read()
    result = rp.can_fetch(headers['User-Agent'], url)
    return result


def get_data(url, num_retries=3, proxies=None):
    try:
        data = requests.get(url, timeout=5)
        print(data.status_code)
    except requests.ConnectionError as e:
        print('请求错误,url:', url)
        print('错误详情:', e)
        data = None
    except:
        print('未知错误,url:', url)
        data = None

    if (data != None) and (500 <= data.status_code < 600):
        if (num_retries > 0):
            print('服务器错误,正在重试...')
            time.sleep(1)
            num_retries -= 1
            get_data(url, num_retries, proxies=proxies)
    return data


"""
python3默认编码为unicode，由str类型进行表示。二进制数据使用byte

     decode                 encode
byte ---------> str(Unicode) ---------> byte

即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
总得意思:想要将其他的编码转换成utf-8必须先将其解码成unicode然后重新编码成utf-8,它是以unicode为转换媒介的
"""


def parse_data(data):
    if data == None:
        return None
    # 因为默认的文本字符串为unicode格式，因此文本字符串没有decode方法
    # 先把unicode的str字符串编程成utf-8的byte类型,再用decode 'utf-8'的编码类型转化成unicode
    charset = chardet.detect(data.content)
    data.encoding =charset['encoding']
    html_text = data.text
    # print(html_text)
    # print(type(html_text))
    interesting_data = re.findall('<title>(.*?)</title>', html_text)
    return interesting_data


if __name__ == '__main__':
    headers = get_headers()
    proxies = get_proxies()
    data = get_data('https://www.baidu.com/', num_retries=3, proxies=proxies)
    interesting_data = parse_data(data)
    print(interesting_data)