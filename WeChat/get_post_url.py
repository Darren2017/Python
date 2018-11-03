import requests
import json
import re
import random
import time

def main():
    idlist = ['microbiota-health']
    posts_url = []

    url = 'https://mp.weixin.qq.com'
    header = {
        "HOST": "mp.weixin.qq.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        }

    with open('cookie.txt', 'r') as f:
        cookie = f.read()
    cookies = json.loads(cookie)

    response = requests.get(url=url, cookies=cookies, headers=header)
    token = re.findall(r'token=(\d+)', str(response.url))[0]

    for query in idlist:
        query_id = {
            'action': 'search_biz',
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'query': query,
            'begin': '0',
            'count': '5',
        }

        search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
        search_response = requests.get(search_url, cookies=cookies, headers=header, params=query_id)

        lists = search_response.json().get('list')[0]
        fakeid = lists.get('fakeid')
        query_id_data = {
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': '0',
            'count': '5',
            'query': '',
            'fakeid': fakeid,
            'type': '9'
        }
        appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
        appmsg_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)

        max_num = appmsg_response.json().get('app_msg_cnt')
        num = int(int(max_num) / 5)
        begin = 0
        try:
            while num + 1 > 0 :
                query_id_data = {
                    'token': token,
                    'lang': 'zh_CN',
                    'f': 'json',
                    'ajax': '1',
                    'random': random.random(),
                    'action': 'list_ex',
                    'begin': str(begin),
                    'count': '5',
                    'query': '',
                    'fakeid': fakeid,
                    'type': '9'
                }
                print('------------------------第',begin,'页-------------------------')
                query_fakeid_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
                time.sleep(random.randint(1,6))
                fakeid_list = query_fakeid_response.json().get('app_msg_list')
                for item in fakeid_list:
                    posts_url.append(item.get('link'))
                    print(item.get('title'))
                num -= 1
                begin+=5
        finally:
            with open('post_url.txt', 'w+') as f:
                f.write(json.dumps(posts_url))


if __name__ == '__main__':
    main()
