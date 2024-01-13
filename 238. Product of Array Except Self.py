class Solution(object):
    # def productExceptSelf(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     n = len(nums)

    #     # Initialize left and right arrays
    #     left = [1] * n
    #     right = [1] * n
    #     res = [1] * n

    #     # Populate left array
    #     for i in range(1, n):
    #         left[i] = left[i - 1] * nums[i - 1]

    #     # Populate right array
    #     for i in range(n - 2, -1, -1):
    #         right[i] = right[i + 1] * nums[i + 1]

    #     # Calculate the product excluding self for each element
    #     for i in range(n):
    #         res[i] = left[i] * right[i]

    #     return res
    
    #O(1) space
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Initialize left and right arrays
        n = len(nums)
        res = [1] * n

        # Populate left array
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # Populate right array
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * right
            right *= nums[i]

        return res
    