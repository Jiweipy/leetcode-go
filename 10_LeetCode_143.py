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
        mid = self.get_middle_node(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def get_middle_node(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def mergeList(self, l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            l1_temp = l1.next
            l2_temp = l2.next

            l1.next = l2
            l1 = l1_temp
            current.next = l1

            l2.next = l1
            l2 = l2_temp
            current = l2

        return dummy.next


if __name__ == '__main__':
    valuesA = [1, 2, 3, 4, 5]
    valuesB = [1, 2, 3, 4, 5]
    valuesC = [6, 7, 8]

    headA = createLinkedList(valuesA)
    headB = createLinkedList(valuesB)
    headC = createLinkedList(valuesC)

    solution = Solution()
    # intersecnode = solution.reorderList(headA)
    # print(intersecnode)
    # listA = convertLinkedListToList(intersecnode)
    # print(listA)

    listA = solution.mergeList(headB, headC)
    listA = convertLinkedListToList(listA)
    print(listA)
