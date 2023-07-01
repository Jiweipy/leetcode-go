"""给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 用一个指针指向当前不重复的元素，遍历数组，如果当前元素与指针指向的元素不同，则将当前元素赋值给指针指向的元素，指针后移一位
        # 2. 遍历结束后，指针指向的位置即为不重复元素的个数
        # 3. 时间复杂度O(n)，空间复杂度O(1)
        if len(nums) == 0:
            return 0
        pointer = 0
        for i in range(1, len(nums)):
            if nums[pointer] != nums[i]:
                pointer += 1
                nums[pointer] = nums[i]
            else:
                continue
        return pointer + 1


if __name__ == '__main__':
    solution = Solution()
    # nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    del_nums_length, del_nums = solution.removeDuplicates(nums)
    print("{0}, nums = {1}".format(del_nums_length, del_nums))
