# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid = n//2+1
        start = 1
        end = n
        while start < end:
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1
            mid = (start+end)//2
        return mid
    
        