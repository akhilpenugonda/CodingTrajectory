class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = 1
        res = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-':
                res += sign * num  # Update result with the current number
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                # Save current result and sign before entering the new scope
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                # Calculate result within the parentheses and update the result
                res += sign * num
                res *= stack.pop()  # Pop the sign
                res += stack.pop()  # Pop the saved result before the parentheses
                num = 0

        # Add the last number to the result
        return res + sign * num
