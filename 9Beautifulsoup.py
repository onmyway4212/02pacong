from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')
# print(soup)
# presttify()的作用是给html代码分好格式
# print(soup.prettify())
# print(soup.title)               <title>The Dormouse's story</title>
# print(soup.title.name)             title
# print(soup.title.string)             The Dormouse's story
# print(soup.title.parent.name)           head
# print(soup.p)                       <p class="title"><b>The Dormouse's story</b></p>
# print(soup.p['class'])                  ['title']
# print(soup.a)                           <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# print(soup.find_all('a'))
# print(soup.find(id='link3'))            <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
"""
从文档中找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))
"""
# 获取所有文字内容
# print(soup.get_text())
# print(soup.text)
'''
# Tag对象
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'lxml')
tag = soup.b
print(tag)
print(tag.name)
tag.name = 'blockquote'
print(tag)
print(tag['class'])
print(tag.get('class'))
print(tag.attrs)
# tag属性可以被添加删除修改,tag的属性操作和字典一样
tag['class'] = 'verybold'
tag['id'] = 1
print(tag)
'''

