import requests
from bs4 import BeautifulSoup
import re
import asyncio
import aiohttp

def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

@asyncio.coroutine
async def fillfile(url):

# def fillfile(url):
    html = gethtmltext(url)
    soup = BeautifulSoup(html, "html5lib")
    # try:
    #     title = soup.find_all('h1')[2].text
    # except:
    #     title = " "
    # print(title)
    # try:
    #     author_date = soup.find_all('div', class_='cz')[0].text
    # except:
    #     author_date = " "
    # print(author_date)
    # try:
    #     artical = soup.find_all('div', class_='normal_intro')[0].text
    # except:
    #     artical = " "
    # print(artical)
    try:
        with open(soup.find_all('h1')[2].text + '.txt', 'w+') as f:
            f.write("标题：" +soup.find_all('h1')[2].text + '\n')
            f.write("作者：" + soup.find_all('div', class_='cz')[0].text + '\n')
            f.write("内容：" + soup.find_all('div', class_='normal_intro')[0].text + '\n')
        print("标题：", soup.find_all('h1')[2].text + '\n')
    except:
        pass

def get_urls(url):
    html = gethtmltext(url)
    soup = BeautifulSoup(html, "html5lib")
    links = []
    for i in soup.find_all('a', href=re.compile('info/')):
        link = i.get('href')
        if link:
            links.append("http://imd.ccnu.edu.cn/" + link.replace('../../', ''))
    return links

def get_next_url(url):
    html = gethtmltext(url)
    soup = BeautifulSoup(html, "html5lib")
    next_urls = []
    for i in soup.find_all('a', class_='Next'):
        link = i.get('href')
        if link:
            link = "http://imd.ccnu.edu.cn/xwdt/xydt/" + link.replace('xydt/', '')
            next_urls.append(link)
    return next_urls

if __name__ == "__main__":
    base_url = "http://imd.ccnu.edu.cn/xwdt/xydt.htm"

    next_urls = get_next_url(base_url)
    for next_url in next_urls:
        b = get_next_url(next_url)
        for w in b:
            if w not in next_urls:
                next_urls.append(w)
                print("翻页链接" + w)

    post_urls = []
    for i in next_urls:
        a = get_urls(i)
        for w in a:
            if w not in post_urls:
                post_urls.append(w)
                print("新闻地址" + w)

    loop = asyncio.get_event_loop()
    tasks = [fillfile(url) for url in post_urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
