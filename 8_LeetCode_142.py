"""

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

题解：https://leetcode.cn/problems/linked-list-cycle-ii/description/

"""


from utils import ListNode, createLinkedList, convertLinkedListToList


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 相遇
            if slow == fast:
                p = head
                q = slow
                while p != q:
                    p = p.next
                    q = q.next
                return p
        return None


if __name__ == '__main__':
    valuesA = [3, 2, 0, -4, 2]
    valuesB = [1, 2]
    headA = createLinkedList(valuesA)
    headB = createLinkedList(valuesB)

    solution = Solution()
    intersecnode = solution.detectCycle(headA)
    print(intersecnode)

