from array import array
import math

class Vector2d:
    typecode = 'd'          # 类属性

    def __init__(self, x, y):           # 构造器
        self.__x = float(x)          # 实例属性
        self.__y = float(y)

    @property
    def x(self):                        # 不支持属性修改，保证数据的可散列性
        return self.__x

    @property
    def y(self):                        # 不支持属性修改，保证数据的可散列性
        return self.__y

    def __iter__(self):                 # 迭代器，用于拆包等
        return (i for i in (self.x, self.y))

    def __hash__(self):             # 哈希  让示例变为可散列的（于__eq__一起）
        return hash(self.x) ^ hash(self.y)

    def __repr__(self):             # 面向程序员的显示
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):              # 面向用户的显示
        return str(tuple(self))

    def __bytes__(self):            # 生成字节序列，而且要为支持用字节序列生成向量做准备
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):        # 用于 == 运算
        return tuple(self) == tuple(other)

    def __abs__(self):              # 用于 abs()
        return math.hypot(self.x, self.y)

    def __bool__(self):             # 用于 bool()
        return bool(abs(self))

    @classmethod                # 类方法
    def frombytes(cls, octets):             # 备选构造器，通过字节序列来生成一个实例
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_sepc=''):          # 格式化显示
        if fmt_sepc.endswith('p'):
            fmt_sepc = fmt_sepc[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_sepc) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.x, self.y)


class Demo:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    @classmethod
    def func_class(cls, *args):
        print(*args)
    
    @staticmethod
    def func_static(*args):
        print(*args)