# -*- coding: utf-8 -*-
# @Time : 2023/11/4 下午10:13
# @Author : Jiwei Qin
# @FileName: 15_LeetCode_2.py
# @Software: PyCharm

"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy_node = ListNode()
    current = dummy_node

    carry = 0
    while l1 or l2 or carry:
        carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        current.next = ListNode(carry % 10)

        carry = carry // 10
        current = current.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy_node.next


if __name__ == '__main__':
    values1 = [2, 4, 3]
    values2 = [5, 6, 4]

    values1_link = ListNode(values1[0])
    current1 = values1_link
    for i in range(1, len(values1)):
        current1.next = ListNode(values1[i])
        current1 = current1.next

    values2_link = ListNode(values2[0])
    current2 = values2_link
    for i in range(1, len(values2)):
        current2.next = ListNode(values2[i])
        current2 = current2.next

    result = addTwoNumbers(values1_link, values2_link)

    current = result
    result_list = []
    while current:
        result_list.append(current.val)
        current = current.next

    print(result_list)



