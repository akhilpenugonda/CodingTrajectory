function validPalindrome(s) {
    function isPalindromeRange(i, j) {
        while (i < j) {
            if (s[i] !== s[j]) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    
    for (let i = 0, j = s.length - 1; i < j; i++, j--) {
        if (s[i] !== s[j]) {
            return isPalindromeRange(i + 1, j) || isPalindromeRange(i, j - 1);
        }
    }
    return true;
}
