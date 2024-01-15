class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Method 1: Using Pivot
        # Time Complexity: O(logn)
        # Space Complexity: O(1)
        # Find pivot
        pivot = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                pivot = i
                break
        # Binary Search
        def binary_search(nums, target, start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(nums, target, start, mid-1)
            else:
                return binary_search(nums, target, mid+1, end)
        if pivot == 0:
            return binary_search(nums, target, 0, len(nums)-1)
        else:
            if target >= nums[0]:
                return binary_search(nums, target, 0, pivot-1)
            else:
                return binary_search(nums, target, pivot, len(nums)-1)

