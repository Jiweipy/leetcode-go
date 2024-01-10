# -*- coding: utf-8 -*-
# @Time : 2023/11/4 下午8:23
# @Author : Jiwei Qin
# @FileName: 13_LeetCode_206.py
# @Software: PyCharm

"""

反转链表

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

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




if __name__ == '__main__':
    values = [1, 2, 3, 4]

    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next

    result = reverseList(head)

    current = result
    while current:
        print(current.val, end=",")
        current = current.next