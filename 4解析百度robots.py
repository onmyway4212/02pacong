import urllib.robotparser


rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://www.baidu.com/robots.txt')
rp.read()

t = rp.can_fetch('Googlebot', 'https://www.baidu.com/baidu')
a = rp.can_fetch('Baiduspider', 'https://www.baidu.com/ulink?')
c = rp.can_fetch('Baiduspider', 'https://www.baidu.com/cpro')
print(t)
print(a)
print(c)

