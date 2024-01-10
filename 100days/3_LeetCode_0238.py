"""238. 除自身以外数组的乘积
中等

给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]

"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results_list = [0] * len(nums)
        results_list[0] = 1
        for i in range(1, len(nums)):
            results_list[i] = results_list[i-1] * nums[i-1]
        print(results_list)
        current_multi = 1
        for i in reversed(range(len(nums))):
            results_list[i] = results_list[i] * current_multi
            current_multi = current_multi * nums[i]
        print(results_list)




if __name__ == '__main__':
    solution = Solution()
    nums = [-1,1,0,-3,3]
    print(solution.productExceptSelf(nums))

