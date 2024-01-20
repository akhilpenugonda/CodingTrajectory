class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. Remove leading spaces
        s = s.strip()
        # 2. Handle empty string
        if not s:
            return 0
        # 3. Handle signs
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        # 4. Convert to integer
        res = 0
        for c in s:
            if not c.isdigit():
                break
            res = res * 10 + int(c)
        # 5. Handle out of range
        res = sign * res
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31
        return res