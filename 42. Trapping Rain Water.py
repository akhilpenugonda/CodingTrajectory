class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointers
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0

        while left < right:
            len_left = height[left]
            len_right = height[right]
            if len_left < len_right:
                if len_left >= left_max:
                    left_max = len_left
                else:
                    res += left_max - len_left
                left += 1
            else:
                if len_right >= right_max:
                    right_max = len_right
                else:
                    res += right_max - len_right
                right -= 1
        return res