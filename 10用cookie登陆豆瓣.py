import requests
from fake_useragent import UserAgent

# 浏览器中复制出来的cookie
mycookie = 'gr_user_id=1592aaf5-d56d-40f4-bb3b-eb4228d90079; ll="118172"; ' \
           '_ga=GA1.2.920441306.1447605906; __utmv=30149280.6566; _vwo_uuid_v2' \
           '=3BD08C536850A19BD7FAAF48DCC42D53|9a1b950d998c0c6c922adabc08da362b;' \
           ' bid=pbNLwyfpcu8; ue="88186161@qq.com"; __yadk_uid=quYYyvRDAhBsgA5IZAiz2eD11vnsPgA8;' \
           ' viewed="25779298_26274202_26692466_27028517_10561367_26713240_25957237_' \
           '26740503_26869992_27061630"; douban-fav-remind=1; ap=1; _pk_ref.100001.8cb4' \
           '=%5B%22%22%2C%22%22%2C1531638019%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DINLSQyg' \
           '-QzqISEeN6puWnV7ReiLaRZ0SKlh5g1gkv4vIyc6qR0oVLWl7L7eR08L5%26wd%3D%26eqid%' \
           '3Db9bedfe600063b57000000035b4af0fb%22%5D; _pk_ses.100001.8cb4=*; __utma=' \
           '30149280.920441306.1447605906.1531547130.1531638021.55; __utmc=30149280; ' \
           '__utmz=30149280.1531638021.55.50.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;' \
           ' __utmt=1; _gid=GA1.2.1375652515.1531638170; ps=y; dbcl2="65660395:6+AWQRD11zU";' \
           ' ck=W2yQ; push_doumail_num=0; douban-profile-remind=1;' \
           ' _pk_id.100001.8cb4=c03a328201a446dc.1456832658.38.1531638210.1531488879.;' \
           ' push_noty_num=0; __utmb=30149280.8.9.1531638210496'

ua = UserAgent()
headers = {'User-Agent': ua.random,
           'Cookie': mycookie,
           }
# 豆瓣个人主页
url = 'https://www.douban.com/people/onmyway4212/'
data = requests.get(url, headers=headers)

print(data.status_code)
print(data.request.headers)
print(data.text)