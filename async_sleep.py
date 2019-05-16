import asyncio
import time
import concurrent.futures as cf

def myfun(i):
    print('start {}th'.format(i))
    time.sleep(1)
    print('finsh {}th'.format(i))

async def main():
    with cf.ThreadPoolExecutor(max_workers=10) as executor:
        loop = asyncio.get_event_loop()
        futures = (loop.run_in_executor(executor, myfun, i) for i in range(10))
        for result in await asyncio.gather(*futures):
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())