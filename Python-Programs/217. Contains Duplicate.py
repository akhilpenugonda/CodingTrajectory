class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Method 1: Using set
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # if len(nums) == 0:
        #     return False
        # else:
        #     return len(nums) != len(set(nums))
        
        # Method 2: Using dictionary
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if len(nums) == 0:
            return False
        else:
            dict = {}
            for i in nums:
                if i in dict:
                    return True
                else:
                    dict[i] = 1
            return False


