"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

"""


class Solution(object):
    # def removeElement(self, nums, val):
    #     """
    #     :type nums: List[int]
    #     :type val: int
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     pointer = 0
    #     right = 0
    #     while right < n:
    #         if nums[right] != val:
    #             nums[pointer] = nums[right]
    #             pointer += 1
    #         right += 1
    #     return pointer

    def removeElement_best(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        right = len(nums)
        left = 0
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return left

    def removeElement_python(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)


if __name__ == '__main__':
    nums1 = [3, 2, 2, 3]
    val1 = 3
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    nums3 = [1, 2, 3, 4]
    val3 = 2
    solution = Solution()

    # result = solution.removeElement(nums2, val2)
    # print(result)

    # result_best = solution.removeElement_best(nums3, val3)
    # print(result_best)

    result_python = solution.removeElement_python(nums3, val3)
    print(result_python)
