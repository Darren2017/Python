from time import sleep, strftime
from concurrent import futures

def display(*args):
    print(strftime('[%H:%M:%S]'), end='')
    print(*args)

def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10

def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(10))
    display('result:', results)
    display('Waiting for individual results:')
    for i, results in enumerate(results):
        display('result{}: {}'.format(i, results))

main()


def tiems(timer):
    def decorator(func):
        def wrapper(*arg, **kwarg):
            s_time = time.time()
            func()
            e_time = time.time()
            print '函数耗时%s' % (e_time - s_time)
            

def times(timer):

    @wraps(func)
    def wrapper(*arg, **kwarg):
        s_time = time.time()
        func()
        e_time = time.time()
        print '函数耗时%s' % (e_time - s_time)
    return wrapper