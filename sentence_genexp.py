import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    '''fifth edition of Sentence'''
    
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):         //返回一个生成器
        '''如果函数或构造方法只有一个参数，传入的生成器表达式时不用写一对调用函数的括号，
        再写一对括号围住生成器表达式，只写一对括号就可以'''
        return (match.group() for match in RE_WORD.finditer(self.text))