class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. Brute Force
        # def isPalindrome(s):
        #     return s == s[::-1]
        # if not s: return ""
        # res = s[0]
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         if isPalindrome(s[i:j+1]) and j-i+1 > len(res):
        #             res = s[i:j+1]
        # return res
        # 2. Expand Around Center
        if not s: return ""
        res = ""
        for i in range(len(s)):
            # odd case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(res):
                res = s[l+1:r]
            # even case
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(res):
                res = s[l+1:r]
        return res
        # 3. Dynamic Programming
        # if not s: return ""
        # res = s[0]
        # dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        # for i in range(len(s)):
        #     dp[i][i] = True
        # for i in range(len(s)-1, -1, -1):
        #     for j in range(i+1, len(s)):
        #         if s[i] == s[j]:
        #             if j - i < 3 or dp[i+1][j-1]:
        #                 dp[i][j] = True
        #                 if j - i + 1 > len(res):
        #                     res = s[i:j+1]
        # return res
        # 4. Manacher's Algorithm
        # if not s: return ""
        # s = "#" + "#".join(s) + "#"
        # res = s[0]
        # dp = [0 for _ in range(len(s))]
        # center = right = 0
        # for i in range(1, len(s)-1):
        #     if i < right:
        #         dp[i] = min(right-i, dp[2*center-i])
        #     while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
        #         dp[i] += 1
        #     if i + dp[i] > right:
        #         center = i
        #         right = i + dp[i]
        #     if dp[i] > len(res):
        #         res = s[i-dp[i]:i+dp[i]+1]
        # return res.replace("#", "")