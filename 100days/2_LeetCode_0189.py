"""给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

"""


class Solution(object):
    def rotate(self, nums: list, k:int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 报错原因：modify nums in-place instead
        # trans_list = nums[len(nums)-k:]
        # swap_list = nums[:len(nums)-k]
        # nums = trans_list + swap_list
        # print(nums)

        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,-100,3,99]
    print(solution.rotate(nums, 2))

