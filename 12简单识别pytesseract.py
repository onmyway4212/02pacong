import pytesseract
from PIL import Image
import time

image_names = ['111.jpg','22.jpg','33.jpg','44.jpg','555.jpg','666.jpg',
               '777.jpg','888.jpg','1010.jpg','douban.jpg',]

for image_name in image_names:
    image = Image.open(image_name)
    vcode = pytesseract.image_to_string(image, lang='chi_sim')
    # 弹出这张图片
    Image._show(image)
    time.sleep(1)
    print('正在识别...{}的内容...\n'.format(image_name))
    print(vcode)
    print('{}已打印完成!\n'.format(image_name))
    print('*'*50)
    time.sleep(1)