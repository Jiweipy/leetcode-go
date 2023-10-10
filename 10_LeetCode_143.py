"""

给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


"""


from utils import ListNode, createLinkedList, convertLinkedListToList


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """




if __name__ == '__main__':
    valuesA = [3, 2, 0, -4, 2]
    valuesB = [1, 2]
    headA = createLinkedList(valuesA)
    headB = createLinkedList(valuesB)

    solution = Solution()
    intersecnode = solution.reorderList(headA)
    print(intersecnode)

