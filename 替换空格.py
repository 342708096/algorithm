# -*- coding:utf-8 -*-
'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为Python is a useful language.则经过替换之后的字符串为Python%20is%20a%20useful%20language.

同时可以将替换字符变成变量， 用任意字符替换空格

同时还可以设置被替换字符为变量，替换任意字符
'''

'''
方法一：
对字符串逐一判断并替换

方法二：
利用字符串的replace函数

'''

class Solution_1:

    def replace_space(self, source_string, replace_item):
        # 判断源字符串是否为string
        if not isinstance(source_string, str):
            return None
        # 如果源字符串是None， 返回None
        if source_string == None:
            return None
        # 如果源字符串是‘’， 返回‘’
        if len(source_string) == 0:
            return ''
        # 如果替换字符非字符串或是None或者‘’，返回源字符串
        if not isinstance(replace_item, str) or replace_item == None or len(replace_item) == 0:
            return source_string

        result_string = ''
        # 逐一判断是不是空格，如果是空格则替换
        for string_item in source_string:
            if string_item.isspace():
                result_string += replace_item
            else:
                result_string += string_item
        return result_string


# test data
str_1 = 'Python is a useful language.'
str_2 = ''
str_3 = '  '
str_4 = None
str_5 = 1

replace_1 = '%20'
replace_2 = ''
replace_3 = None
replace_4 = 1
test = Solution_1()
print test.replace_space(str_1, replace_1)
print test.replace_space(str_1, replace_2)
print test.replace_space(str_1, replace_3)
print test.replace_space(str_1, replace_4)

print test.replace_space(str_2, replace_1)
print test.replace_space(str_3, replace_1)
print test.replace_space(str_4, replace_1)
print test.replace_space(str_5, replace_1)
