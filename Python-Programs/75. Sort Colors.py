class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        # 1. Counting Sort
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        # Counting Sort is a linear time sorting algorithm that sort in O(n+k) time when elements are in range from 1 to k.
        # Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing).
        # Then doing some arithmetic to calculate the position of each object in the output sequence.

        dict = {0:0, 1:0, 2:0}
        for i in nums:
            dict[i] += 1
        nums[:dict[0]] = [0] * dict[0]
        nums[dict[0]:dict[0]+dict[1]] = [1] * dict[1]
        nums[dict[0]+dict[1]:] = [2] * dict[2]

        # 2. Dutch National Flag Problem
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        # The problem was posed with three colours, here `0′, `1′ and `2′. The array is divided into four sections:
        # a[1..Lo-1] zeroes (red)
        # a[Lo..Mid-1] ones (white)
        # a[Mid..Hi] unknown
        # a[Hi+1..N] twos (blue)
        # The unknown region is shrunk while maintaining these conditions
        # Lo := 1; Mid := 1; Hi := N;
        # while Mid <= Hi do
        #     Invariant: a[1..Lo-1]=0 and a[Lo..Mid-1]=1 and
        
                