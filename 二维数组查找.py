# -*- coding:utf-8 -*-
'''
题目：
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
方法一：
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况

方法二：
利用in一直查找

如果出现了array中既有字符串,又有数字,可能需要用到ord()函数
'''
import unittest

class Solution_1:
    def Find(self, array, target):

        # 初始化标识变量
        find_flag = False
        # 判断是否为空数组，若是直接返回无结果
        if array == None or len(array) == 0:
            return find_flag
        # 得到二维数组的行和列
        row_num = len(array)
        col_num = len(array[0])
        # 右上角坐标
        row = 0
        col = col_num - 1
        # 从右上角开始遍历
        # 如果发现，直接返回结果
        # 如果target小于数组元素向左移一位
        # 如果target大于数组元素向下移一位
        while (col >= 0) and (row < col_num):
            if array[row][col] == target:
                find_flag = True
                break
            elif array[row][col] > target:
                col = col - 1
            else:
                row = row + 1
        return find_flag


class Solution_2:
    def Find(self, array, target):

        # 初始化标识变量
        find_flag = False

        # 判断是否为空数组，若是直接返回无结果
        if array == None or len(array) == 0:
            return find_flag

        # 利用in直接查找
        for array_index in range(len(array)):
            if target in array[array_index]:
                find_flag = True
        return find_flag



# 测试数据
array = [[1, 3, 5, 7],
         [2, 4, 6, 8],
         [3, 5, 7, 9],
         [4, 6, 8, 10]]
array_2 = []
array_3 = None
array_4 = [[62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],
           [63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],
           [64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],
           [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],
           [66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],
           [67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]]

find_target = Solution_1()
print find_target.Find(array, 9)
print find_target.Find(array, 12)
print find_target.Find(array_2, 9)
print find_target.Find(array_3, 9)
print find_target.Find(array_4, 9)
print find_target.Find(array_4, 62)

find_target = Solution_2()
print find_target.Find(array, 9)
print find_target.Find(array, 12)
print find_target.Find(array_2, 9)
print find_target.Find(array_3, 9)
print find_target.Find(array_4, 9)
print find_target.Find(array_4, 62)


# Test Code
class TestSolution(unittest.TestCase):

    def test_solution_1(self):
        find_target_1 = Solution_1()
        print 'test solution_1 start'
        self.assertEquals(find_target_1.Find(array, 9), True)
        self.assertEquals(find_target_1.Find(array, 12), False)
        self.assertEquals(find_target_1.Find(array_2, 9), False)
        self.assertEquals(find_target_1.Find(array_3, 9), False)
        self.assertEquals(find_target_1.Find(array_4, 62), True)
        print 'test solution_1 end'

    def test_solution_2(self):
        find_target_2 = Solution_2()
        print 'test solution_2 start'
        self.assertEquals(find_target_2.Find(array, 9), True)
        self.assertEquals(find_target_2.Find(array, 12), False)
        self.assertEquals(find_target_2.Find(array_2, 9), False)
        self.assertEquals(find_target_2.Find(array_3, 9), False)
        self.assertEquals(find_target_2.Find(array_4, 62), True)
        print 'test solution_2 end'