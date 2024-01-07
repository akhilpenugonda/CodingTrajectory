class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
#         # Method 1: Brute Force
#         # Time: O(n)
#         # Space: O(n)
        # intervals.append(newInterval)
        # intervals.sort()
        # res = []
        # for interval in intervals:
        #     if res == [] or res[-1][1] < interval[0]:
        #         res.append(interval)
        #     else:
        #         res[-1][1] = max(res[-1][1], interval[1])
        # return res    
    
#         # Method 2: Binary Search
#         # Time: O(logn)
#         # Space: O(n)
        def binarySearch(intervals, newInterval):
            low = 0
            high = len(intervals) - 1
            while low <= high:
                mid = (low + high) // 2
                if intervals[mid][0] == newInterval[0]:
                    return mid
                elif intervals[mid][0] < newInterval[0]:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        index = binarySearch(intervals, newInterval)
        intervals.insert(index, newInterval)
        res = []
        for interval in intervals:
            if res == [] or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
    
        