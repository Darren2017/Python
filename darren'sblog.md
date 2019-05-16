标题:  符合Python风格的对象
连接:  https://darren2017.github.io/2018/10/12/符合Python风格的对象/

向量类Vector2d类是自定义的一个python类，实现了一些基础的魔法方法，透过这个类可以对python的类进行一定的了解。
1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162from array import arrayimport mathclass Vector2d:    typecode = 'd'          # 类属性    def __init__(self, x, y):           # 构造器        self.__x = float(x)          # 实例属性        self.__y = float(y)    @property    def x(self):                        # 不支持属性修改，保证数据的可散列性        return self.__x    @property    def y(self):                        # 不支持属性修改，保证数据的可散列性        return self.__y    def __iter__(self):                 # 迭代器，用于拆包等        return (i for i in (self.x, self.y))    def __hash__(self):             # 哈希  让示例变为可散列的（于__eq__一起）        return hash(self.x) ^ hash(self.y)    def __repr__(self):             # 面向程序员的显示        class_name = type(self).__name__        return '{}({!r}, {!r})'.format(class_name, *self)    def __str__(self):              # 面向用户的显示        return str(tuple(self))    def __bytes__(self):            # 生成字节序列，而且要为支持用字节序列生成向量做准备        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))    def __eq__(self, other):        # 用于 == 运算        return tuple(self) == tuple(other)    def __abs__(self):              # 用于 abs()        return math.hypot(self.x, self.y)    def __bool__(self):             # 用于 bool()        return bool(abs(self))    @classmethod                # 类方法    def frombytes(cls, octets):             # 备选构造器，通过字节序列来生成一个实例        typecode = chr(octets[0])        memv = memoryview(octets[1:]).cast(typecode)        return cls(*memv)    def __format__(self, fmt_sepc=''):          # 格式化显示        if fmt_sepc.endswith('p'):            fmt_sepc = fmt_sepc[:-1]            coords = (abs(self), self.angle())            outer_fmt = '<{}, {}>'        else:            coords = self            outer_fmt = '({}, {})'        components = (format(c, fmt_sepc) for c in coords)        return outer_fmt.format(*components)    def angle(self):        return math.atan2(self.x, self.y)
@classmethod与@staticmethod123456789class demo:    @classmethod    def func_class(cls, *args):        print(cls)        print(*args)        @staticmethod    def func_static(*args):        print(*args)
@classmethod第一个参数接受类本身，而不是实例本身。所以被 @classmethod装饰的函数都是类方法，只能对类进行操作，不能对实例进行操作。具体可以参照第一个代码的使用。   
@staticmethod与普通的方法没有太大的区别，唯一的区别就是定义的地方不一样而已。
格式化显示内置的format()函数和str.format()方法都会调用.__format__(format_spec)方法。在没有实现__format__方法时，会返回str(my_object)。具体的format()使用方法在此不具体讲解。 
__slots__类属性
使用__slots__将所有的实例属性存储到一个可迭代对象中，从而避免使用消耗内存的__dict__属性。   
但是缺点是在类中定义了__slots__属性之后，实例不能拥有__slots__之外的属性。另外，不要把__dict__属性也放到__slots__中，原因太明显了。  
用户自定义的类中默认有__weakref__属性，但是如果使用了__slots__记得将其放进去，否则该类将不再支持弱引用。  
__slots__属性不可以继承。

覆盖类属性12Vector2d.typecode = 'b'v1.typecode = 'b'   # v1是Vector2d的一个实例
第一种方式修改类属性，第二种方式用实例属性去覆盖类属性。
--------------------------------------




标题:  木犀后端机试准备
连接:  https://darren2017.github.io/2018/09/21/木犀后端机试准备/

请先按照–>>引导<<–安装虚拟机shell基础
ls 

介绍： 查看当前文件内容
示例 


cd[目录]

介绍： 切换文件路径，其后可加当前文件之下的路径，也可以加绝对路径
选项内容
-表示上次所在路径
.表示当前目录
..表示上一层目录，这个经常用
ps: 按下Tab键提示可以切换的下层路径。


示例 


vim [文件名]

当输入的文件名存在时，则打开文件，并可以进行编辑，注意文件的后缀也要输入。
当输入的文件名不存在时，则新建文件并打开进行编辑，注意文件的后缀也要输入。
进入vim后，键入i进入编辑模式，此时终端的左下角或右下角出现-- INSERT --字样，标志处于编辑模式。
编辑完成后键入Esc退出编辑模式，此时键入:，进入vim的命令模式，输入w、q分别代表保存和退出，可以同时输入，但要注意顺序。



第一个Python程序通过vim新建并编辑一个hello.py程序，退出后输入python hello.py便可以运行程序。
在上述示例中我们新建了一个python程序，该程序的功能是打印输入“hello muxi”，并且我们成功运行了它。
结语机试的引导部分到此结束，希望大家提前做完引导部分，为机试做好准备工作。最后祝大家机试顺利。
--------------------------------------




标题:  对象引用、可变性和垃圾回收
连接:  https://darren2017.github.io/2018/09/20/对象引用、可变性和垃圾回收/

变量
python变量不是盒子，是标注。
创建在前，分配在后。是把变量分配给对象，而不是把对象分配给变量。
一个对象可以分配多个标签，而一个标签只能贴到一个对象上。

is与==
==运算符比较两个对象的值，调用对象的__eq__方法。如果是自定义类型，并且没有重载__eq__方法，则==会比较两个对象的id–标识。
is比较对象的id。
在变量和单例值之间比较时应该使用is，特别是检查变量绑定的值是不是None时。因为is方法不能被重载，速度更快。不用像==那样去寻找有没有重载__eq__方法。

元组的相对不可变性tuple虽然被划分为不可变序列，但是相对于str而言，tuple的不可变性又有自己的特点。对于不可变序列在tuple直接保存，而对于可变序列则保存引用。
1234567891011import sys			//改变元组内可变序列的值，而元组的内存占用并没有改变。t1 = (1, 2, [30, 40])t2 = (1, 2, 3, 4, 5, [30, 40])print("the memory of ", t1, " = ", sys.getsizeof(t1))print("the memory of ", t2, " = ", sys.getsizeof(t2))t1[-1].append([1,2,3,4,5,6,7,8])print("the memory of ", t1, " = ", sys.getsizeof(t1))
由此我们可以得出，其实元组真的是不可变的。元组内只是保存了可变序列的引用，而我们修改的也是可变序列的值，并没有修改它的标识。所以某种程度上元组的值并没有改变……….
深拷贝与浅拷贝这是一个好网站，网站的动画演示非常到位，可以把下面的代码输进去试一下。
12345678910l1 = [3, [66, 55, 44], (7, 8, 9)]l2 = list(l1)l1.append(100)l1[1].remove(55)print('l1: ', l1)print('l2: ', l2)l2[1] += [33, 22]l2[2] += (10, 11)print('l1: ', l1)print('l2: ', l2)
__deepcopy__deepcopy()会调用__deepcopy__方法来进行深拷贝。深拷贝时对于可变与不可变序列都会创建新的对象，而不是增加引用。deepcopy函数会记住已经复制的对象，因此能优雅的处理循环引用。
函数的参数函数的参数不能是可变序列函数的参数不能是可变序列函数的参数不能是可变序列函数的参数不能是可变序列重要的事情说三遍！！！
12345678910111213141516class HauntedBus:    def __init__(self, passagers=[]):        self.passagers = passagers    def pick(self, name):        self.passagers.append(name)    def drop(self, name):        self.passagers.remove(name)bus1 = HauntedBus()bus1.pick('darren')bus2 = HauntedBus()print(bus1.passagers)print(bus2.passagers)
在HauntedBus中，passagers的默认值是一个空列表，也可以说它引用了一个空列表。当我们对这个空列表做增删操作时，使得其中的值发生改变。但是注意的是之后所有的HauntedBus实例中，passagers都是引用了同一个列表，因此之后创建的所有实例，其passagers属性都不为空。   
防御可变参数当传入的参数是可变序列是，并且我们要修改它的内容，但是不希望对原值产生影响。这时我们便需要注意一些事项，可以选择用工厂函数产生这个参数的副本，对其副本进行操作，便可以避免对原参数产生影响。这里可以类比C语言中的值传递和指针传递（也可以是名字传递）。
1234567891011121314151617181920class HauntedBus:    def __init__(self, passagers=None):        if passagers is None            self.passagers = []        else            self.passagers = list(passagers)            # self.passagers = passagers			# “错误”操作    def pick(self, name):        self.passagers.append(name)    def drop(self, name):        self.passagers.remove(name)bus1 = HauntedBus()bus1.pick('darren')bus2 = HauntedBus()print(bus1.passagers)print(bus2.passagers)
垃圾回收
对象绝不会自行销毁；然而，无法得到对象时，可能会被当作垃圾回收。

del
del命令可能会导致对象被当作垃圾回收，但是更多的时候仅仅是删除对象的一个引用。   
Cpython2.0增加的分代垃圾回收算法，可以检测引用循环中涉及的对象组，如果一组对象之间相互引用，导致无法获取，则被回收。
一般情况下我们不需要显示地调用del函数，python会帮我们做好内存回收工作。

弱引用引用对象，但不增加对象的引用计数。
1234567891011121314import weakrefa_set = {0, 2}wref = weakref.ref(a_set)       # 增加一个弱引用，但是不会增加对象的引用计数wref()a_set = {3, 5, 6}wref()                  # 之所以可以继续得到{0, 2}是因为在控制台中，{0, 2}与_变量绑定，增加了引用计数wref() is None          # 执行过后True与_绑定，{0, 2}的引用计数为零，被回收。wref()      _wref() is None
--------------------------------------




标题:  字典和集合
连接:  https://darren2017.github.io/2018/09/12/字典和集合/

字典字典的key必须是可散列的数据类型，实现了__hash__()和__qe__()方法。
字典推导字典推导可以从任何以键值对作为元素的可迭代对象中构建出字典。
12345dial = [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')]dic = {key : value for key , value in dial}print (dic)
setdefault类似于collections.defaultdict，在查询不到key时不会抛出异常而是返回默认值。
12345dial = [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')]dic = {key : value for key , value in dial}print (dic.setdefault('nokey', 'notfoundvalue')
__missing__所有的映射类型在处理找不到的键时，都会牵扯到__missing__方法。基类dict虽然没有提供该方法，但是如果一个类继承了dict，并且提供__missing__方法，那么在__getitem__找不到键时便会自动调用__missing__方法。
1234567891011class mydict(dict):    def __missing__(self, key):        self[key] = 'default'        print('调用missing方法')        return 'default'    test = mydict()test['key'] = 'value'print (test['key'])print (test['nokey'])
另外__missing__方法只会被__getitem__调用，不会被get或者__contains__调用。
collections.OrderDict添加键的时候会保持顺序，因此键的迭代次序可以保持一致。popitem（）方法默认删除最后一个添加的键值对，提供参数last=False时删除第一个。
collections.ChainMap1234567from collections import ChainMapx = {'a': 1, 'b': 2}y = {'b': 10, 'c': 11}z = ChainMap(y, x)for k, v in z.items():        print(k, v)
collections.UserDict用纯Python的方式把标准的dict实现了一遍，提供给用户继承写子类。但collections.UserDict并不是dict的子类。
不可变映射类型MappingProxyType可以返回一个只读的映射试图，并且是动态的。我们可以通过这个代理访问到源映射但是无法作出修改，从而保证了数据的安全性。
1234567from types import MappingProxyTypedic = {"key":"value"}dic_proxy = MappingProxyType(dic)print(dic_proxy["key"])dic_proxy["newkey"] = "newvalue"
字典的特点
内存开销大，散列表是稀疏数组导致了大内存的开销。
键查询速度快。
往字典里添加新建可能会导致已有键的顺序改变。—-那么如何避免这个问题呢？

集合论集合中的元素必须是可散列的，set类型本身是不可散列的。集合的本质是许多唯一对象的集合，因此集合可以用于去重。接受一个可迭代对象去掉重复部分。
12set([1,2,3,4,5,6,6,5,4,3,2,1])set("google")
中缀运算符：
| 合集
& 交集
- 差集
^ 对称差
in 属于
<= 包含于
< 真包含于

集合推导12l = [1,2,3,4,5,6,6,5,4,3,2,1]s = {i for i in l if i < 5}
集合的其他方法
s.add(e) 添加
s.clear() 清空
s.copy() 浅复制
s.discard(e) 移除，不存在不抛出异常
s.remove(e) 异常，不存在抛出异常
s.pop()    随机移除，不存在抛出异常

集合的特点
元素必须是可散列的。
内存开销大，由上一条特点导致。
可以高效的判断元素是否存在某一个集合中。
元素次序取决于添加次序
添加新元素可能破坏原有次序。

散列表
散列表是一个稀疏数组（总是有空白的数组称为稀疏数组）。散列值在理想情况下越是相似，他们的散列值差别越大。
盐值：盐值是python进程中的一个常量，每次启动Python解释器生成的盐值都不相同。盐值主要用于计算对象的散列值。在计算散列值时随机加盐可以防止DOS攻击。
散列表的算法：略
可散列的条件：
支持hash()函数，并且通过__hash__()方法得到的散列值是不变的（同一次启动解释器中不变，加盐的原因不同次不相等）
支持通过__eq__()方法来检测相等性。
如a == b则hash(a) == hash(b)



--------------------------------------




标题:  序列构成的数组
连接:  https://darren2017.github.io/2018/09/08/序列构成的数组/

序列类型容器序列list、tuple、collections.deque等序列可以存放不同类型的数据。
扁平序列str、bytes、bytearray、memoryview、array.array等序列只能容纳一种类型。
可变序列list、bytearray、memoryview、array.array、collections.deque
不可变序列tuple、str
列表列表推导列表推导（真的好用）是构建list的快捷方式，但劲酒虽好，不要贪杯哦！列表推导虽然好用，但是不要过度的使用，保持代码的简短，超过两行可以考虑使用for循环。
12345colors = ['black', 'white']sizes = ['S', 'M', 'L']tshirts = [(color, size) for color in colors for size in sizes]tshirts
生成器表达式相较于列表推导，生成器表达式背后遵守了迭代器协议，可以逐个地产出元素，而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里，如果我们需要的列表很大时，用列表推导的方式不仅耗费时间还耗费内存，而生成器表达式则避免了这个问题。
1234567891011121314151617import sysL = [x for x in range(3000) if x % 2]		//列表推导J = (x for x in range(3000) if x % 2)		//生成器表达式countL = 0countJ = 0for x in L:	countL += 1	for x in J:	countJ += 1	print("countL == ",countL, "     countJ == ",countJ)		//可见二者的效果是一样的print(sys.getsizeof(J),  sys.getsizeof(L))		//在内存占用上二者的差距还是很大的
切片格式：swq[start:stop:step]内部调用__getitem__(slice(start:stop:step))方法。切片是个好东西，但是突然发现没的说………..
序列的+与*这东西好用，但是有坑，据我所知GGH夏令营就被这个坑过，所以如果不熟悉慎用之。因为*有时并没有创建新的元素，而是增加了已有元素的引用。  
1234567board = [['-'] * 3 for i in range(3)]board[1][2] = 'X'boardweird_board = [['-'] * 3 ] * 3		//这是一个坑weird_board[1][2] = 'X'board
另外也可以使用sys.getsizeof(obj)来查看内存的占用，这里边有一个很有意思的事情。多改变几次数值，观察下内存的变化，你会发现一件很有意思的事情，可以猜想下为什么会有这种变化。 
1234567mylist = [1, 2, 3, 4, 5]test = [mylist] * 30mylisttestsys.getsizeof(mylist)sys.getsizeof(test)
排序list.sort就地排序，改变原序列的值并且返回None
sorted不改变原序列的值，生成一个新的列表，可以接受任何形式的可迭代对象作为参数。
共同点：两个可选关键字参数   

reverse：默认值为False，如果设置为True，则被排序的序列会以降序输出。  
key：只有一个参数的函数。这样的方式体现了一种编写API的思想，将API的功能交给调用方来确定，使得相应的API更加灵活。

查找与插入bisect模块主要包含两个主要函数，bisect和insort，两个函数都利用二分查找算法在有序序列中查找或插入元素
1234bisect.bisect_left(t,x) #在T列表中查找x，若存在，返回x左侧位置bisect.bisect_right(t,x)bisect.insort_left(t,x) #在T列表中查找X，若存在，插入x左侧；bisect.insort_right(t,x)
元组元组常被称为不可变的列表，但初此之外元组还可以用于没有字段名的记录。
元组拆包
元组拆包可以应用到任何可迭代对象上，唯一的硬性要求是被可迭代对象中元素的数量必须要跟接受这些元素的元组的空档数一致，另外可以用*来忽略多余的元素，也可以使用_占位符，来忽略某几个元素。   
接受表达式的元组可以是嵌套式的，但接受元组的嵌套结构必须符合表达式本身的嵌套结构。  

与列表的不同除了跟增减元素相关的方法之外，元组支持列表的其他所有方法。例外是元组没有__reversed__方法，但是仍然可以使用reversed(tuple)。
--------------------------------------




标题:  Python数据模型
连接:  https://darren2017.github.io/2018/09/07/Python数据模型/

collectionscollections是Python内建的一个集合模块，提供了许多有用的集合类。
namedtuple具名元组，tuple的一个子类。能够用来创建类似于tuple的数据类型，除了能够用索引来访问数据，能够迭代，更能够方便的通过属性名来访问数据。类似于tuple，namedtuple的属性也是不可改变的。
123456from collections import namedtuple	Card = collections.namedtuple('Card', ['rand', 'suit'])	beer_card = Card('7', 'diamonds')print(beer_card.rand, beer_card[0])
dequedeque是高效实现了插入和删除操作的双向列表，适合用于队列和栈。相较而言list可以按索引快速访问元素，但是插入和删除元素则很慢，因为list是现行存储，数据量大的时候，插入和删除效率很低。
12345678from collections import dequesq = deque([str(x) for x in range(10)])sq.append('x')		//入栈 or 入队sq.pop()				//出栈sq.appendleft('y')	sq.popleft()			//出队
defaultdict安全的字典。使用dict时，如果引用的key不存在，则会抛出KeyError，如果希望key不存在时不抛出Error而是返回一个默认值，则可以使用deafultdict
1234567from collections import defaultdictdedict = defaultdict({'key':'value'},lambda: 'not found')dedict['key'] = 'value'dedict['key']dedict['nokey']
OrderedDict在dict中，key是无序的，所以当我们对dict做迭代时顺序是不确定的。当我们需要一个确定的顺序时可以使用OrderedDict。OrderedDict中key的排序是按照插入顺序排序。   
CounterCounter是一个简单的计数器，并且只存储次数大于一的元素，否则可以访问，但是不存储。
12345678from collections import Counterc = Counter()c['d']for str in 'mycounter':  	c[str] += 1c
特殊方法
通常我们无需直接使用特殊方法，直接调用特殊方法的频率应该远远低于我们去实现他们的次数。通过内置函数（例如len、iter、str，等等）来使用特殊方法是最好的选择。这些内置函数不仅会调用特殊方法，通常还提供额外的好处，而且对于内置的类来说，他们的速度更快。    ————《Fluent Python》

__getitem____getitem__方法的实现使得我们可以像p[key]这样来取值。并且我们通过索引来访问元素时也是使用了__getitem__方法。
__len__当我们使用len(obj)函数来获取一个对象的长度时，便是调用了__len__方法。
__repr__ or __str__简单来说这两个方法都是用于显示的，但是__str__是面向用户的，__repr__是面向程序员的。在使用str()或者是print()时候会首先调用__str__方法，并且这种方法返回的字符串对终端用户更友好。在没有实现__str__方法时，两个函数回去调用__repr__方法。如果两个方法二选一去实现，显而易见后者是我们的选择。
__enter__ and __exit__用于上下文管理，简单讲解见这里。
附录
跟运算符无关的特殊方法  
根运算符相关的特殊方法 

Others其他的特殊方法还有很多，与以上集中特殊方法各有异同，能力有限，时间有限不做过度描述。
--------------------------------------




标题:  Flask_个人进阶
连接:  https://darren2017.github.io/2018/09/04/Flask-个人进阶/

首先感谢老板的课程，上午刚看了个这门课，虽然想学但是奈何没钱买啊！然后下午老板就给买了…..幸福来的太突然。之前用“狗书”学过 Flask， 这次看完课程感觉有些比较新的东西，总结一下，不想看完就忘了。  
pipenv在看这门课程之前一直是用virtualenv来做虚拟环境的管理，感觉还挺好用的。但是课程中七月老师用的是pipenv，相比较而言感觉pipenv确实挺好用的。相比较之下virtualenv总会出一下小问题，比如生成requirements的时候会不怎么特别好用，虽说无关痛痒，但是也挺烦人的。下面列举几个pipenv常用的命令：  

Linux与MacOS下的安装方式sudo pip install pipenv   ||   brew install pipenv
创建or安装虚拟环境pipenv install [--two || --three] 
使用可选参数指定python的版本，否则使用默认版本。  
Pipenv会在项目文件夹下自动寻找Pipfile和Pipfile.lock文件，创建一个新的虚拟环境并安装必要的软件包。如果没有找到Pipfile和Pipfile.lock则创建一个新的虚拟环境。


安装第三方库pipenv install module
卸载第三方库pipenv uninstall module
进入虚拟环境pipenv shell
打包输出第三方库pipenv lock
退出虚拟环境exit

add_url_rule一般情况下我们都使用@route()这个装饰器来注册路由， 实际上@route()内部也是调用了add_url_rule方法来进行路由注册。通常情况下我们都使用装饰器的方式进行路由注册，这种方式也符合我们的书写和阅读习惯。但是有一种情况下必须add_url_rule方式，即使用类做视图函数时。   

@route()内部实现:
1234567891011121314151617181920def route(self, rule, **options):    """Like :meth:`Flask.route` but for a blueprint.  The endpoint for the    :func:`url_for` function is prefixed with the name of the blueprint.    """    def decorator(f):        endpoint = options.pop("endpoint", f.__name__)        self.add_url_rule(rule, endpoint, f, **options)        return f    return decorator    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):    """Like :meth:`Flask.add_url_rule` but for a blueprint.  The endpoint for    the :func:`url_for` function is prefixed with the name of the blueprint.    """    if endpoint:        assert '.' not in endpoint, "Blueprint endpoints should not contain dots"    if view_func and hasattr(view_func, '__name__'):        assert '.' not in view_func.__name__, "Blueprint view function name should not contain dots"    self.record(lambda s:        s.add_url_rule(rule, endpoint, view_func, **options))
  视图函数存储在flask核心对象的view_functions中，key是endpoint,value为视图函数。当endpoint为空时，把视图函数名赋值给endpoint。规则存放在url_map中。

使用add_url_rule方式注册路由：    
12345678910from flask import Flask    app = Flask(__name__)    # @app.route('/')def index():    return 'index!'    app.add_url_rule('/', view_func=index)if __name__ == '__main__':


if __name__ == __main__有点不想写这个，但是七月老师特地提到了这个就写一下吧。在python中当一个函数被直接运行时，他的__name__属性会是__main__, 所以加上这个会保证一个python程序作为一个包被导入时不会直接运行，否则这个python程序中如果有什么可以直接运行的顶级代码，则会直接运行，而不是等待调用。
flask框架结构
一个flask核心对象–app
一个核心对象下包含一个或多个蓝图
一个蓝图下包含一个或多个视图函数

上下文什么是上下文实现了__enter__和__exit__方法的对象。当我们需要对一个对象添加不属于它的一些属性和方法时，我们便可以设计一个上下文，把新的参数和原有对象放到上下文中，生成一个新的对象。
AppContextAppContext是对flask核心对象的封装，
RequestContent当有一个新的request产生时，flask会生成一个RequestContent，在RequestContent推入_request_ctx_stack栈之前，flask会检查_app_ctx_stack的栈顶，如果栈顶为空或者不是当前对象，flask会把AppContent推入_app_ctx_stack栈中，之后将RequestContent推入_request_ctx_stack中。所以说我们在写测试代码的时候会产生RuntimeError: Working outside of application context错误，这时只需要手动将一个AppContent推入栈中即可。   
with1234567891011class MyResource:    def __enter__(self):        print('connect db')        return self    def __exit__(self):        print('close db)        return True	with Myresource() as re:    pass

re的值为__enter__方法返回的值，with Myresource() as re:语句会执行__enter__方法中的内容。
当with语句结束或出现异常时会执行__exit__方法中的内容。如果__exit__返回False则会抛出异常，如果返回True则不会抛出异常。

配置文件在七月老师的课程中提出来配置文件可以分成两类，一类是公开的可以上传到GitHub上的，另一类是隐私性的，需要写在gitignore中。之前我们的做法都是隐私的数据写成环境变量用os来读取，但是我经常碰到os读取不到的问题，所以感觉这种方式也不错，相对在服务器的环境变量中配置到不如在服务器中新开一个私密配置文件。所需要的信息依然写在README中。
线程与进程一种思想
看了七月老师课感觉收获最大的是一种思想。同样是程序，可能实现的功能是一样的，但是感觉七月写的真的有种很优美的感觉，如果自己去写就太粗糙了。    
代码写了不仅是用来运行的，很大程度上是用来看的，不仅是给自己看，更多时候是给别人看（几个月之后看自己的代码和别人的可能没啥区别，所以说对自己好一点）。所以写一个优雅的程序真的很重要，起码现在我写完的程序我是绝对不想去碰第二次的，太痛苦了。   
七月的课程中体现了一种拆分的思想，试图函数越简单越好，把逻辑实现放在其他地方。有时候一个功能很简单，可能直接写在试图函数中了，但最好的做法是用一个“函数”去实现。阅读者只需要看你的函数名便知道你要做什么，不要“强迫”阅读者去看你全部的源程序。
面向对象的方式编程。课程中面向对象的方式看着很优雅，而我一直在用面向过程的方式，可能对面向对象还不是那么熟悉，以后也要尽量尝试用面向对象的方式。所以说课程中很对面向对象的地方处理的很优雅，但是能力有限就没有总结，之后有机会再写。

--------------------------------------




标题:  basic_algorithm
连接:  https://darren2017.github.io/2018/07/24/basic-algorithm/

第一次参加ACM协会的活动，接触了一些算法，总结一些。
前缀和
定义：给定一个数组A[1..n]，前缀和数组PrefixSum[1..n]定义为：PrefixSum[i] = A[0]+A[1]+…+A[i-1];
用途：对数据做预处理简化之后的操作，降低时间复杂度。
示例：求两个整数a到b之间的所有数字的各个位数中1出现的次数，代码 

尺取法
简介：尺取法通常是对数组保存一对下标，即所选取的区间的左右端点，然后根据实际情况不断地推进区间左右端点以得出答案。之所以需要掌握这个技巧，是因为尺取法比直接暴力枚举区间效率高很多，尤其是数据量大的时候，所以尺取法是一种高效的枚举区间的方法，一般用于求取有一定限制的区间个数或最短的区间等等。当然任何技巧都存在其不足的地方，有些情况下尺取法不可行，无法得出正确答案。
OJ
program
套路
12345678910111213int r, l = 0;while(1){	while(当前区间不满足条件&&r<n){		r++;		更新区间信息；	}	if(当前区间不满足条件){		break;	}	更新ans；	l++;	更新区间信息；}


二分法
简介：顾名思义，二分法采取了二分的思想，因此二分法也具有较为理想的时间复杂度–O(logn)。但是二分法也有自己的要求，首先是数据储存在数组中，链表无法使用，再就是数据必须是有序的。
OJ
program
套路：
123456789101112void find(){    int l = max, r = n * max;	//根据具体情况确定两个边界    while(l < r){        int mid = (l + r) / 2;        if(check(mid) == 1){            r = mid;        }else{            l = mid + 1;        }    }    printf("%d\n", l);}


这一段基本是固定的，主要难点就是check函数怎么写。
DFS
简介：深度优先搜索，从当前节点出发；依次访问与该节点相连的节点，按照深度优先的原则，直至找到结果或者判断条件不成立时返回上一层继续往下进行搜索。返回后要做标记，避免重复访问，进行回溯。
OJ
program

BFS
简介：广度优先搜索，经常用于检索最短路径。与队列相互配合使用，注意每次元素入栈后立即标记该元素被访问而不是真正被访问后再标记。路径的记录可以采用一些特殊的方法，目前只会几种简单的，所以不记录了。
OJPOJ - 3414
program
套路
12345678910111213141516int bfs(int x, int y){   	queue<pair<int, int> > q;	q.push(make_pair(x, y));	v[y][x] = 1;	s[y][x] = 0;	while(!q.empty()){	    tp = q.front();	    q.pop();	    if(条件满足){	        return 结果;	    }else{	    	遍历所有与该节点相邻的节点，如果满足条件放入队列尾部，并标记已访问	    }	}	return 0;}

--------------------------------------




标题:  木犀星计划--shell入门
连接:  https://darren2017.github.io/2018/07/23/木犀星计划-shell入门/

写在开始之前
首先欢迎大家参加木犀星计划，希望你们可以顺利完成星计划成为木犀实习生，加入我们木犀大家庭。
此博客主要介绍一些常用的Linux基础命令，命令不是很复杂，但是很有趣，也需要大家去记忆，希望你在看这篇博的的时候身边有一台可以使用的Linux或macOS电脑。这样可以跟着教程做练习，提高学习效率。
如果你是Ubuntu系统可以先使用系统自带的bash，日后可以去探索其他的shell。如果你是macOS推荐使用 oh my zsh , 至于 oh my zsh 的安装教程大家可以去网上搜索，也算是对大家动手能力一种测试。

常用命令
ls[选项][参数] 

介绍： 查看文件内容，参数可选
选项内容：

-a 显示全部内容   ps:以.开头的文件/文件夹是隐藏的
-l 查看详情


示例 





cat[内容]
介绍：显示文件内容
示例：cat starplan.md显示starplan文件中的内容




cd[目录]
介绍： 切换文件路径，其后可加当前文件之下的路径，也可以加绝对路径
选项内容
~表示家目录
/表示根目录
-表示上次所在路径
pwd查看当前路径的绝对路径
.表示当前目录
..表示上一层目录 
ps:  看到这里你可能会觉得是不是...表示上上层目录啊！抱歉似乎这种骚操作Linux不支持，不过macOS是支持的，而且你也可以使用....作用和你想的一样


示例 




touch[内容]
介绍：创建新的文件
示例：touch test.cpp创建test.cpp文件


mkdir[内容]
介绍： 创建新的文件夹
示例：mkdir starplan创建starplan文件夹


rm[内容][参数]

介绍：删除文件/文件夹
选项内容：
-r递归处理，将指定目录下的所有文件与子目录一并处理
-f强制删除文件或目录
ps：指定被删除的文件列表，如果参数中含有目录，则必须加上-r选项，最暴力的是加-rf,不过慎用，除非你确定你所选择的目录是你想要删除的。


示例：rm test.md删除test.md文件


cp[选项][原文件目录][目标目录]

介绍：复制文件/目录
选项介绍
-r复制目录
-p连文件属性一起复制


示例：cp pots.cpp ~/Documents/将pots.cpp文件移动到家目录下的Document文件夹下


mv[原文件目录][目标文件目录]
介绍：移动文件/目录+文件/目录重命名，移动命令和cp使用类似，此处不过多介绍，重命名功能只需要将第二个选项改为自己想要的新名字即可
示例：mv backend muxi将backend重命名为muxi


whereis[选项] [命令名]
介绍：查找命令
选项介绍
-b 只查找可执行文件
-m 只查找帮助文件


示例： 


shutdown[选项][时间]
介绍：关机和重启
选项介绍
-c 取消前一个关机命令
-h 关机
-r 重启


时间介绍：
+分钟 于几分钟后关机/重启
详细时间 于某一事件关机/重启
now 立刻关机/重启


示例：shutdown -h now立刻关机   



写在最后本博客中所写的命令中参数并未全部列出，只是给出了基础的常用的，你可以尝试在命令后加--help查看具体可选参数
--------------------------------------




标题:  木犀星计划--Linux虚拟机安装
连接:  https://darren2017.github.io/2018/07/19/木犀星计划-Linux虚拟机安装/

为什么要用Linux
身为一个程序员的你还在用Windows不觉得很low吗？难道你对黑黑的terminal（终端）没有一丝向往吗？
其次使用Windows做开发会带来许多不便，许多Windows上难以解决的难题在Linux上几条命令便可以轻松解决
如果经济条件允许Macbook Pro当然是首选，至于air可以先不考虑了。如果没过Mac也不用灰心，正常的开发需有Ubuntu（Linux目前最流行的一个版本）完全可以搞定

为什么用虚拟机
双系统当然是首选，但是星计划期间不推荐大家装双系统，毕竟涉及到硬件，把电脑搞坏了有点得不偿失，所以推荐大家先玩玩虚拟机。星计划期间虚拟机完全可以满足你的需要。
如果你是大佬，敢于自己尝试双系统，那也欢迎你，电脑坏了不要找我啊 

开始虚拟机的安装
我们选用VMware来运行我们的Ubuntu
准备工作
Ubuntu16.04镜像
ps: 下载镜像不要进中文官网，直接用英文的，选择桌面版（Desktop），如果下载失败给大家准备了百度云资源，至于下载慢的问题，你可以考虑破解百度云，很简单的。或者自己找镜像资源也可以。
VMware14
VMware许可证：FF31K-AHZD1-H8ETZ-8WWEZ-WUUVA


下载好VMware后开始安装工作
选择安装位置，推荐不要安装在C盘，增强型键盘驱动程序可以不选
检查更新和用户体验可以勾掉


安装Ubuntu18.04
点击创建新的虚拟机
选择安装程序光盘映像文件，并找到我们下载的Ubuntu18.04镜像
填写自己虚拟机的信息，密码不要忘记
选择系统的安装位置，推荐不要放在C盘
选择内存大小，推荐40G，其实都好啦，一开始并不会占用这么多存储空间，而是随着你的使用而逐渐扩大，有一天你发现存储空间不够用了也是可以扩大的，这个不会有影响，但是如果你在尝试双系统建议开大点，因为双系统是不可以后期扩充的
自定义硬件部分，如果你的电脑8G+内存(如果你的电脑还是4G内存，学长友情推荐加个内存条吧，你不会后悔的)推荐4G内存比较合适，处理器分配两个，这个后期也可以调整。
到这里Ubuntu虚机的安装成功结束，你可以启动虚拟机体验Ubuntu了，PS：学长在windows的虚拟机里做的演示步骤只能进行到这里了，毕竟在虚拟机里装另一个虚拟机这个想法还是不好玩的，也装不了。



写在最后如果你在安装过程遇到什么问题欢迎问你的学长学姐，但更希望你可以自己Google解决，自己解决问题的能力也是非常重要的，星计划也非常看重你们这方面的能力。为了你能成功解决问题，学长送你一把梯子，让你看看墙外的世界。 以下是梯子的参数：   



参数
参数值




IP
45.77.90.112


端口
80


密码
muxi


加密方式
aes-256-ctr


协议
auth_sha1_v4


混淆
tls1.2_ticket_auth



--------------------------------------




