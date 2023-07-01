"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """



if __name__ == '__main__':
    solution = Solution()
    nums = [1,0,1,1,0,1]
    nums1 = [1,1,0,1,1,1]
    one_nums = solution.removeElement(nums)
    # one_nums_best = solution.findMaxConsecutiveOnes(nums)
    print(one_nums)
    # print(zero_nums_best)
