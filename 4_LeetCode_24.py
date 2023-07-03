# Definition for singly-linked list.
"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
"""


from utils import ListNode, createLinkedList, convertLinkedListToList

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        时间复杂度：O(n)，其中 n 是链表的节点数量。需要对每个节点进行更新指针的操作。
        空间复杂度：O(n)，其中 n 是链表的节点数量。空间复杂度主要取决于递归调用的栈空间
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        """
        对于两个相邻节点head和head.next，我们需要将它们交换位置。
        为此，我们首先将head.next赋值给newHead，这样newHead就成为新的头节点。
        然后，我们将newHead.next指向原来的head，即交换了两个节点的位置。
        """
        newHead = head.next
        # newHead.next = head   # 报错：RecursionError: maximum recursion depth exceeded

        rest = head.next.next
        head.next = self.swapPairs(rest)  # 将当前节点head的下一个节点指向了交换后的剩余部分的头节点

        newHead.next = head
        return newHead

    def swapPairs_noRecursion(self, head: ListNode) -> ListNode:
        """
        时间复杂度：O(n)，其中 n 是链表的节点数量。需要对每个节点进行更新指针的操作。
        空间复杂度：O(1)。
        :param head:
        :return:
        """
        dumpHead = ListNode(0)
        dumpHead.next = head
        temp = dumpHead
        """
        依次交换两个节点: 
            交换之前的节点关系是 temp -> node1 -> node2，
            交换之后的节点关系要变成 temp -> node2 -> node1
        """
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            # 交换链表的两个节点元素
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            # 赋值，进行下一次循环
            temp = node1
        return dumpHead.next


if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    head = createLinkedList(values)

    solution = Solution()
    # swapped = solution.swapPairs(head)

    # result = convertLinkedListToList(swapped)
    # print(result)

    swapped1 = solution.swapPairs_noRecursion(head)
    result1 = convertLinkedListToList(swapped1)
    print(result1)
    # result_best = solution.removeElement_best(nums3, val3)
    # print(result_best)
