"""给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""


class Solution(object):
    # def moveZeroes(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     # O(n2)
    #     pointer = 0
    #     num_len = len(nums)
    #     while pointer < num_len:
    #         if nums[pointer] == 0:
    #             for j in range(pointer, len(nums) - 1):
    #                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
    #             num_len -= 1
    #         else:
    #             pointer += 1
    #     return nums

    def moveZeroes_best(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        left = right = 0
        while right < nums_len:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums




if __name__ == '__main__':
    solution = Solution()
    # nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums1 = [0, 1, 0, 3, 12]
    # zero_nums = solution.moveZeroes(nums)
    zero_nums_best = solution.moveZeroes_best(nums)
    # print(zero_nums)
    print(zero_nums_best)
