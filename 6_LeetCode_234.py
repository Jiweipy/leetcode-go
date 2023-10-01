"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
"""


from utils import ListNode, createLinkedList, convertLinkedListToList


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        申请一个容器，然后把元素都放到数组中
        """
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next

        # print(vals[::-1])  # 字符串翻转

        """
        用left和right两个指针，一个往后，一个往前，不断迭代
        如果left的值不等于right说明不是回文，反之是回文
        """
        left = 0
        right = len(vals) - 1
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    valuesA = [4, 1, 8, 1, 4]
    valuesB = [1, 2]
    headA = createLinkedList(valuesA)
    headB = createLinkedList(valuesB)


    solution = Solution()
    intersecnode = solution.isPalindrome(headB)
    print(intersecnode)

