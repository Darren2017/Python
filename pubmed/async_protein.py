import requests
from bs4 import BeautifulSoup
import asyncio
from aiohttp import ClientSession

url_1 = 'https://www.uniprot.org/uniprot/?query=*&offset='
url_2 = '&columns=id%2centry+name%2creviewed%2cprotein+names%2cgenes%2corganism%2clength'

@asyncio.coroutine
async def get_name_of_page(url):
    try:
        async with ClientSession() as session:
            async with session.get(url) as r:
                r = await r.read()
                soup = BeautifulSoup(r, 'html5lib')
                temp = []
                for i in soup.find_all('div', 'long'):
                    if i.get_text():
                        temp.append(i.get_text())
                temp = list(set(temp))
                with open("protein'name.txt", "a+") as f:
                    for i in temp:
                        f.write(i + '\n')
                        print(i)
    except:
        print("********************* error ******************8")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [get_name_of_page(url_1 + str(i * 25) + url_2) for i in range(1, 100)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
