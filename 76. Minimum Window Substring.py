class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # approach using sliding window
        # Time: O(n)
        l, r = 0, 0
        res = ''
        count = 0
        min_len = float('inf')
        t_count = collections.Counter(t)
        while r < len(s):
            if s[r] in t_count:
                t_count[s[r]] -= 1
                if t_count[s[r]] >= 0:
                    count += 1
            while count == len(t):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]
                if s[l] in t_count:
                    t_count[s[l]] += 1
                    if t_count[s[l]] > 0:
                        count -= 1
                l += 1
            r += 1

        return res

