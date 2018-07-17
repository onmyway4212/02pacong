import requests, re
import pickle
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from PIL import Image


def get_cookie_from_net():
    url = 'https://accounts.douban.com/login'
    login_html = s.get(url, headers=headers).text
    # 找到验证码的图片网站,并且保存为douban.jpg
    verif_img_url = re.findall(r'<img id="captcha_image" src="(.*?)" alt="captcha"', login_html)[0]
    verif_img_data = s.get(verif_img_url, headers=headers).content
    with open('douban.jpg', 'wb') as f:
        f.write(verif_img_data)

    img = Image.open('douban.jpg')
    Image._show(img)
    captha_img = str(input("输入验证码:"))
    captha_id = re.findall(r'name="captcha-id" value="(.*?)"/>', login_html)[0]
    print('captcha_id:', captha_id)

    # captcha-solution是图片的验证码内容
    # captcha-id是一个双重验证,可以在登陆页面找到
    payload = {
        'source': 'None',
        'redir': 'https://www.douban.com/',
        'form_email': '88186161@qq.com',
        'form_password': 'zh1234567',
        'captcha-solution': captha_img,
        'captcha-id': str(captha_id),
        'login': '登录',
    }

    data = s.post(url, headers=headers, data=payload, verify=True)

    # 把cookies保存到文件里
    with open('cookies.douban', 'wb') as f:
        # requests只能保持 cookiejar 类型的cookie
        # 将CookieJar转为字典
        cookiedict = requests.utils.dict_from_cookiejar(s.cookies)
        pickle.dump(cookiedict, f)
    print('提交表单登陆,成功获取cookies...')

    if '你的用户名' in data.text:
        print("登陆成功!")

    return s.cookies


def get_cookies_from_file():
    with open('cookies.douban', 'rb+') as f:
        cookiedict = pickle.load(f)
        # 将字典转为CookieJar
        cookies = requests.utils.cookiejar_from_dict(cookiedict)
    print('从文件解析cookie成功,提取cookies...')
    return cookies


def getdata(html):
    soup = BeautifulSoup(html.text, 'lxml')
    mydata = soup.select('#intro_display')[0].get_text()
    return mydata


def login_and_getdata():
    print('获取cookies...')
    try:
        s.cookies = get_cookies_from_file()
    except:
        print('从文件获取cookies失败...\n正在尝试提交表单登陆以获取...')
        s.cookies = get_cookie_from_net()
    html = s.get('https://www.douban.com/people/onmyway4212/', headers=headers)
    # print(html.text)
    data = getdata(html)
    print(data)


if __name__ == '__main__':
    s = requests.session()
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    login_and_getdata()

'''
<img id="captcha_image" src="https://www.douban.com/misc/captcha?id=tQCCES0ljppP14fk85lPGbj3:en&size=s" alt="captcha" class="captcha_image">
<input type="hidden" name="captcha-id" value="tQCCES0ljppP14fk85lPGbj3:en">
'''
