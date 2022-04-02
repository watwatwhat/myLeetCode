class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        dup = 0
        while val in nums:
            del nums[nums.index(val)]
            nums.append('_')
            dup += 1
        k = len(nums) - dup
        return k