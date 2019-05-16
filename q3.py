import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):          #队列长度
        return self.num_of_elems

    def is_empty(self):         #判断是否为空
        return (self.num_of_elems == 0)

    def enqueue_first(self, elem):      #队头添加元素
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.front_ind = (self.front_ind - 1) % len(self.data)
            self.data[self.front_ind] = elem
            self.num_of_elems += 1

    def enqueue_last(self, elem):       #队尾添加元素
        if(self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.back_ind = (self.back_ind + 1) % len(self.data)
            self.data[self.back_ind] = elem
            self.num_of_elems += 1

    def dequeue_first(self):        #对头元素出队列
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        elif(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def dequeue_last(self):         #对尾元素出队列
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.back_ind]
        self.data[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        elif(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):            # 取队头元素
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def last(self):             #取队尾元素
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.back_ind]

    def resize(self, new_cap):
        old_data = self.data
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            new_data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.data = new_data
        self.front_ind = 0
        self.back_ind = self.front_ind + self.num_of_elems - 1


'''
q = ArrayDeque()
for i in range(1, 100):
    q.enqueue_first(2*i)
    q.enqueue_last(2*i+1)
while(q.is_empty() == False):
    print(q.dequeue_first())
'''


class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()


from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack():
    def __init__(self):
        self.Stack = ArrayStack()
        self.Deque = ArrayDeque()
        self.__len__ = len(self.Stack) + len(self.Deque)

    def top(self):
        return self.Deque.first()

    def _balance_stack_deque(self):
        if len(self.Stack) < len(self.Deque):
            self.Stack.push(self.Deque.dequeue_last())

    def push(self, value):
        if self.__len__ == 0:
            self.Stack.push(value)
        else:
            self.Deque.enqueue_first(value)
        self._balance_stack_deque()

    def mid_push(self, value):
        self._balance_stack_deque()
        self.Deque.enqueue_last(value)
        self._balance_stack_deque()

    def pop(self):
        if self.Deque.front_ind > 0:
            self.Deque.dequeue_first()
        elif self.Deque.back_ind > 0:
            self.Deque.dequeue_last()
        else:
            self.Stack.pop()


midS = MidStack()
midS.push(2)
midS.push(4)
midS.push(6)
midS.push(8)
midS.mid_push(10)
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())
print('*********')
midS2 = MidStack()
midS.push(2)
midS.push(4)
midS.push(6)
midS.push(8)
midS.push(10)
midS.mid_push(12)
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())