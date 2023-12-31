"""
给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。


"""


from utils import ListNode, createLinkedList, convertLinkedListToList


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        print(seen)
        return False

    def hasCycle_v2(self, head):
        """

        :param head:
        :return:
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    valuesA = [3, 2, 0, -4, 2]
    valuesB = [1, 2]
    headA = createLinkedList(valuesA)
    headB = createLinkedList(valuesB)

    solution = Solution()
    intersecnode = solution.hasCycle(headA)
    print(intersecnode)

