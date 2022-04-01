class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            left_index = 0
            right_index = len(nums) - 1
            while left_index <= right_index:
                middle_index = (left_index + right_index) // 2
                middle_num = nums[middle_index]
                if middle_num > target:
                    right_index = middle_index - 1
                    continue
                if middle_num < target:
                    left_index = middle_index + 1
                    continue
            return left_index