# -*- coding: utf-8 -*-
# @Time : 2023/7/1 下午4:44
# @Author : Jiwei Qin
# @FileName: utils.py
# @Software: PyCharm

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next

    return head


def convertLinkedListToList(head):
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    return values

