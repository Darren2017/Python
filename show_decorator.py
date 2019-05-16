registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def ff():
    print("running ff()")
    
ff()
print(ff.__name__)



def myregister(func):
    def f(*args, **arvgs):
        print('running register(%s)' % func)
        func()
    return f

@myregister
def f1():
    print("running f1")

f1()