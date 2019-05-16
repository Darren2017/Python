import requests
from bs4 import BeautifulSoup
import json
from get_post_url import get_post_url
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'pgv_pvi=5007577088; pt2gguin=o0291534809; RK=+AQoShHQHV; ptcz=9c50057851d839a9d07b992d5305bc3810bf018e17f1694aca3f6feaf211f1d0; ua_id=N48NOHY2r2LLczt1AAAAADosprqB4H9DjfEe6vl92yY=; mm_lang=zh_CN; pgv_si=s9229359104; rewardsn=; wxtokenkey=777',
    'Host': 'mp.weixin.qq.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def fillfile(html, soup, url, i):
    try:
        with open(str(i) + "   " + soup.find('h2', id="activity-name").get_text().split()[0] + '.txt', 'w+') as f:
            f.write("标题：" + soup.find('h2', id="activity-name").get_text().lstrip() + '\n')
            f.write("作者：" + soup.find('span').get_text().lstrip() + '\n')
            f.write("内容：" + soup.find('div', id='js_content').get_text().lstrip() + '\n')
        print("标题：", soup.find('h2', id="activity-name").get_text().lstrip())
    except:
        pass
def get_post():
    # with open('../post_url.txt', 'r') as f:
    #     urls = f.read()
    # urls = json.loads(urls)
    i = 1
    urls = get_post_url()
    for url in urls:
        html = gethtmltext(url)
        soup = BeautifulSoup(html, "html5lib")
        fillfile(html, soup, url, i)
        i += 1

if __name__ == '__main__':
    get_post()