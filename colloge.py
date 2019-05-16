#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import bs4

def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillunvilist(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

def printunvilist(ulist, num):
    print("{:^10}\t{:^6}\t{:^15}\t{:^10}".format("排名", "学校名称", "地区", "得分"))
    for i in range(num):
        u = ulist[i]
        # print(u[0],u[1],u[2],u[3])
        print("{:^10}\t{:^6}\t{:^15}\t{:^10}".format(u[0], u[1], u[2], u[3]))

def main():
    url = "http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2018.html"
    num = 100
    ulist = []
    html = gethtmltext(url)
    fillunvilist(ulist, html)
    printunvilist(ulist, num)
if __name__ == '__main__':
    main()
