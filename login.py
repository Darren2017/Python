import requests
from bs4 import BeautifulSoup

url = "https://account.ccnu.edu.cn/cas/login"

f = requests.get(url)

cookie = f.headers.get('set-cookie')
Cookie = cookie[0:49]
print(Cookie)

soup = BeautifulSoup(f.content, "html.parser")
lt = soup.find('input', {'name' : 'lt'}) ['value']
execution = soup.find('input',{'name' : 'execution'}) ['value']
print ('lt : ', lt)
print ('execution : ', execution)


headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'157',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':Cookie,
    'Host':'account.ccnu.edu.cn',
    'Origin':'https://account.ccnu.edu.cn',
    'Referer':'https://account.ccnu.edu.cn/cas/login',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

data = { 'username' : '2017211661',
         'password' : '',
         'lt' : lt,
         'execution' : execution,
         '_eventId' : 'submit',
         'submit' : '登录'
}

response = requests.post(url, data = data, headers = headers)
print ('Content-Length', response.headers.get('content-length'))
print ('Set-Cookie : ', response.headers.get('set-cookie'))
print ('Expires : ', response.headers.get('Expires'))
print ('Server : ', response.headers.get('server'))
print ('Connection : ', response.headers.get('connection'))
print ('Pragma : ', response.headers.get('pragma'))
print ('Cache-Control : ', response.headers.get('cache-control'))
print ('Date : ', response.headers.get('date'))
print ('Content-Type : ', response.headers.get('content-type'))