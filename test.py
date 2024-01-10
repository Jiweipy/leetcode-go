# -*- coding: utf-8 -*-
# @Time : 2023/11/3 下午11:36
# @Author : Jiwei Qin
# @FileName: test.py
# @Software: PyCharm

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkList(values: list):
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


if __name__ == '__main__':
    values = [1, 3, 5]
    link = createLinkList(values)
    list_values = convertLinkedListToList(link)
    print(list_values)






