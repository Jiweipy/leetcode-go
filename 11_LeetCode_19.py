# -*- coding: utf-8 -*-
# @Time : 2023/11/4 上午10:13
# @Author : Jiwei Qin
# @FileName: 11_LeetCode_19.py.py
# @Software: PyCharm

"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""


# 定义指定结构体
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list2linklist(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next

    return head


class Solution(object):
    def removeNthFromEnd(self, head, n):
        # 使用哑结点
        dummy_node = ListNode(0)
        dummy_node.next = head

        # 快慢指针
        slow = dummy_node
        fast = dummy_node

        #
        for i in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        # 删除节点操作
        del_node_val = slow.next.val
        slow.next = slow.next.next

        return del_node_val, dummy_node


if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    headA = list2linklist(values)

    solution = Solution()
    del_node_val, result = solution.removeNthFromEnd(headA, 2)

    print(del_node_val)

    result_list = []
    current = result
    while current:
        result_list.append(current.val)
        current = current.next
    print(result_list)






