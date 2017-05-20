# -*- coding:utf-8 -*-
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

'''
方法：
需要判断队列是否为空， stack_1负责进栈，stack_2负责出栈

'''

class Solution:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, node):
        self.stack_1.append(node)

    def pop(self):
        if len(self.stack_2) == 0 and len(self.stack_1) == 0:
            return None
        elif len(self.stack_2) == 0:
            while(len(self.stack_1) > 0):
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()



# test data
stack = Solution()
stack.push(1)
stack.push(2)
stack.push(3)
print stack.pop()
stack.push(4)
print stack.pop()
print stack.pop()
print stack.pop()
print stack.pop()