# -*- coding: utf-8 -*-
# @Time : 2023/11/4 上午10:13
# @Author : Jiwei Qin
# @FileName: 12_LeetCode_86.py
# @Software: PyCharm

"""
86. 分隔链表

给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。"""


# 定义指定结构体
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def splitLinkList(head, x):

    small_list = ListNode(0)
    large_list = ListNode(0)
    cur1, cur2 = small_list, large_list

    while head:
        if head.val < x:
            cur1.next = head
            cur1 = cur1.next
        else:
            cur2.next = head
            cur2 = cur2.next

        head = head.next

    cur2.next = None
    # 这里用large_list.next是为了去掉初始化的时候的0节点
    cur1.next = large_list.next

    return small_list.next


if __name__ == '__main__':
    values = [1, 4, 3, 2, 5, 2]
    # values = [2, 1]

    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next

    result = splitLinkList(head, 3)

    result_list = []
    current = result

    while current:
        result_list.append(current.val)
        current = current.next

    print(result_list)









