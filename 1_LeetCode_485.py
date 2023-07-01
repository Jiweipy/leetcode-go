"""
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

时间复杂度：O(n)O(n)，其中 nn 是数组的长度。需要遍历数组一次。

空间复杂度：O(1)O(1)。
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        current_length = 0
        n = len(nums)
        right = 0
        while right < n:
            if nums[right] == 1:
                current_length += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                current_length = 0
            right += 1
        if current_length  > max_length:
            max_length = current_length
        return max_length



if __name__ == '__main__':
    solution = Solution()
    nums = [1,0,1,1,0,1]
    nums1 = [1,1,0,1,1,1]
    one_nums = solution.findMaxConsecutiveOnes(nums)
    # one_nums_best = solution.findMaxConsecutiveOnes(nums)
    print(one_nums)
    # print(zero_nums_best)
