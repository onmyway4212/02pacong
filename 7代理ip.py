import requests

proxies = {
    # 'http': '125.88.74.122:84',
    'https': '94.240.33.242:3128',
    # 'https': '101.236.21.22:8866',
    # 'http': '118.190.95.35:9001',
    # 'http': '122.114.31.177:808',

}
headers = {
	"User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
	"Referer": "http://www.xicidaili.com/nn/1",
}

http_url = "http://www.xicidaili.com/nn/1"
http_u = 'http://icanhazip.com/'

# http://icanhazip.com/ 这个网站显示的是本机ip地址
data = requests.get(http_url, headers=headers, proxies=proxies, timeout=5)

print(data.text)