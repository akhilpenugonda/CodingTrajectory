# validate if string is palindrome


def isPalindrome(s):
    s = s.lower()
    s = "".join(e for e in s if e.isalnum())
    return s == s[::-1]


# character wise comparision using index implementation
# trunk-ignore(ruff/F811)
def isPalindrome(s):
    s = s.lower()
    s = "".join(e for e in s if e.isalnum())
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # trunk-ignore(ruff/E741)
        l = len(s) - 1
        f = 0
        s = s.lower()
        while l >= f:
            if not s[l].isalnum():
                l -= 1
                continue
            if not s[f].isalnum():
                f += 1
                continue
            if s[l] != s[f]:
                return False
            l -= 1
            f += 1
        return True
