import concurrent.futures as cf
import asyncio
import requests
import time
from bs4 import BeautifulSoup

def get_title(i):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i*25)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    lis = soup.find('ol', class_='grid_view').find_all('li')
    for li in lis:
        title = li.find('span', class_='title').text
        print(title)

async def main():
    with cf.ThreadPoolExecutor(max_workers=10) as executor:
        loop = asyncio.get_event_loop()
        futures = (loop.run_in_executor(executor, get_title, i) for i in range(10))
        for result in await asyncio.gather(*futures):
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print('------------------------------')

time.sleep(3)

for i in range(10):
    get_title(i)