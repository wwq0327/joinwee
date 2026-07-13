#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .pinyin.pinyin import PinYin
    
def string2py(string):
    py = PinYin()
    result = py.hanzi2pinyin(string)
    return ''.join(result)

if __name__ == '__main__':
    print(string2py('你好'))
    print(string2py('a你好 ， 呀'))
    print(string2py('hello, The world!'))
    

'''
nihao
anihao，ya
hello,Theworld!
'''
