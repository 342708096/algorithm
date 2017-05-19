# -*- coding:utf-8 -*-
'''
输入一个链表，从尾到头打印链表每个节点的值。
'''

'''
方法一：
使用insert()方法

方法二：
使用append()和reverse()方法

'''

class ListNode:
    def __init__(self, x = None):
        self.val = x
        self.next = None


class Solution_1:

    def ListFromTailToHead(self, ListNode):

        if ListNode.val == None:
            return None

        if ListNode.next == None:
            return ListNode.val

        reverse_list = []

        head = ListNode

        while head:
            # insert(0, item), index = 0 始终设置为第一个元素，类似压栈
            reverse_list.insert(0, head.val)
            head = head.next

        return reverse_list


class Solution_2:
    def ListFromTailToHead(self, ListNode):

        if ListNode.val == None:
            return None

        if ListNode.next == None:
            return ListNode.val

        reverse_list = []

        head = ListNode

        while head:
            reverse_list.append(head.val)
            head = head.next

        reverse_list.reverse()

        return reverse_list

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

single_node = ListNode(12)

no_node = ListNode()

test_1 = Solution_1()
test_2 = Solution_2()

print test_1.ListFromTailToHead(node1)
print test_2.ListFromTailToHead(node1)
print test_1.ListFromTailToHead(single_node)
print test_2.ListFromTailToHead(single_node)
print test_1.ListFromTailToHead(no_node)
print test_2.ListFromTailToHead(no_node)