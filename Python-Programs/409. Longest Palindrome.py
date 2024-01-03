class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        for char in s:
            dict[char] = dict.get(char, 0) + 1
        oddMax = 0
        evenCount = 0
        for val in dict.values():
            if(val % 2 == 0):
                evenCount += val
            else:
                if(val > oddMax):
                    if(oddMax - 1 > 0):
                        evenCount += oddMax - 1 
                    oddMax = val
                else:
                    evenCount += val-1
        return evenCount + oddMax                    