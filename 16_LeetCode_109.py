# -*- coding: utf-8 -*-
# @Time : 2023/11/4 下午10:13
# @Author : Jiwei Qin
# @FileName: 16_LeetCode_109.py
# @Software: PyCharm

"""
有序链表转换二叉搜索树

给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差不超过 1。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMidNode(head):
    fast = slow = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def sortedListToBST(head):
    def buildTree(left, right):
        if left == right:
            return None
        mid = getMidNode(head)
        root = TreeNode(mid)
        root.left = buildTree(left, mid)
        root.right = buildTree(mid.next, right)
        return root

    return buildTree(head, None)


if __name__ == '__main__':
    values = [-10, -3, 0, 5, 9]

    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next

    result = sortedListToBST(head)
    result_list = []
    # while result:
    #     result_list.append(result.val)
    #     result = result.

