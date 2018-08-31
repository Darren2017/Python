import requests     #用python3运行
from bs4 import BeautifulSoup

def gethtmltext(url):           #获取博客内容，用于导入beautifulsoup进行解析
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def makemainurl():
    preurl = "https://"
    namerul = input("input blog's name:  ")     #所爬博客的名字
    namerul = str(namerul)
    surl = ".github.io"                     #构建请求文章的URL
    url = preurl + namerul + surl

    return url

def confirmpage():
    page = input("input the page:  ")           #确定爬取博客的第几页
    if page == '1':
        pages = ""
    else:
        pages = '/page/' + str(page)
    return pages

def fillfile(html, soup, url):
    filename = input('inupt the file\'s name   ')
    f = open(filename + '.md', 'w')
    for link in soup.find_all('a', class_ = "post-title-link"):     #在相应的a标签中获取文章部分链接
        newurl = url + link.get('href')                     #构建文章对应的链接
        newhtml = gethtmltext(newurl)
        newsoup = BeautifulSoup(newhtml, "html.parser")        #将文章链接导入beautifulsoup进行解析
        bodys = newsoup.find('div', class_ = "post-body").get_text()        #获取正文内容
        try:   
            titles = newsoup.find('h1', class_="post-title").get_text()         #获取文章标题--不同的博客title的储存标签不一样，所以用的多个try-except语句进行异常处理
            print("已完成： " + titles)                                           #提示用户正在进行爬取，不然万一用户以为程序卡了怎么办
        except:
            try:
                titles = newsoup.find('h2', class_="post-title").get_text()
                print("已完成： " + titles)
            except:
                try:
                    titles = newsoup.find('h3', class_="post-title").get_text()
                    print("已完成： " + titles)
                except:
                    print("标题添加失败")
                    return 0
        f.writelines("标题:  " + titles + '\n')         #将标题和正文写入文件
        f.writelines("连接:  " + newurl + '\n')
        f.writelines(bodys)
        f.write("--------------------------------------" + '\n' + '\n' + '\n' + '\n' + '\n')

def main():
    url = makemainurl()
    pages = confirmpage()
    html = gethtmltext(url + pages)
    soup = BeautifulSoup(html, "html.parser")   #解析文本
    fillfile(html, soup, url)
    
if __name__ == '__main__':
    main()