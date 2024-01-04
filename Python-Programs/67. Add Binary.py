class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            bitA = int(a[i]) if i >= 0 else 0
            bitB = int(b[j]) if j >= 0 else 0
            sum = bitA + bitB + carry

            result = str(sum % 2) + result
            carry = sum // 2

            i -= 1
            j -= 1

        if carry > 0:
            result = str(carry) + result

        return result