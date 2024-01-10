# -*- coding: utf-8 -*-
# @Time : 2023/11/4 下午8:52
# @Author : Jiwei Qin
# @FileName: 14_LeetCode_92.py
# @Software: PyCharm

"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):

    prev = None
    curr = head

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev



def reverseBetween(head, left, right):

    # 存储翻转列表
    dummy_node = ListNode(-1)
    dummy_node.next = head
    pre = dummy_node

    # 走到 left
    for _ in range(left-1):
        pre = pre.next

    # 走到 right
    right_node = pre
    for _ in range(right-left + 1):
        right_node = right_node.next

    # 切断链表
    left_node = pre.next
    curr = right_node.next
    pre.next = None
    right_node.next = None

    # 翻转链表
    reverseList(left_node)

    #
    pre.next = right_node
    left_node.next = curr

    return dummy_node.next


if __name__ == '__main__':
    values = [1,2,3,4,5]

    headA = ListNode(values[0])
    current = headA
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next

    result = reverseBetween(headA, 2, 4)

    current = result
    while current:
        print(current.val)
        current = current.next

    # print(result)






