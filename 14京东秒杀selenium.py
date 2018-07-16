import time
from selenium import webdriver


def getdata(html):
    pass


def run():
    json_url = 'https://miaosha.jd.com/'
    driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    driver.get(json_url)
    time.sleep(5)

    html = driver.page_source
    print(html)

    data = getdata(html)

    driver.quit()
    return data


if __name__ == '__main__':
    run()