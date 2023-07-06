"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
"""


from utils import ListNode, createLinkedList, convertLinkedListToList

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """

        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return Non




if __name__ == '__main__':
    valuesA = [4, 1, 8, 4, 5]
    valuesB = [5, 6, 1, 8, 4, 5]
    headA = createLinkedList(valuesA)
    headB = createLinkedList(valuesB)

    solution = Solution()
    # swapped = solution.swapPairs(head)

    # result = convertLinkedListToList(swapped)
    # print(result)

    intersecnode = solution.getIntersectionNode(headA, headB)
    print(intersecnode)
    # result_best = solution.removeElement_best(nums3, val3)
    # print(result_best)
