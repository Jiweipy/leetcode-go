"""

给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。

第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。

请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。

你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。


"""


from utils import ListNode, createLinkedList, convertLinkedListToList


class Solution(object):
    def oddEvenList(self, head):
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
    intersecnode = solution.oddEvenList(headA)
    print(intersecnode)

