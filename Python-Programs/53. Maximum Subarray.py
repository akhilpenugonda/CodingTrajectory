class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = nums[0]
        maxSoFar = nums[0]
        for i in range(1, len(nums)):
            currMax = max(nums[i], currMax + nums[i])
            maxSoFar = max(maxSoFar, currMax)
        return maxSoFar