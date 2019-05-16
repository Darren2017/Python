def aritprog_gen(begin, step, end = None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index

def chain(*iterables):
    for i in iterables:
        yield from i

from random import randint

def d6():
    return randint(1, 6)

d6_iter = iter(d6, 6)
for roll in d6_iter:
    print(roll)

//d6_iter_false = iter(d6)