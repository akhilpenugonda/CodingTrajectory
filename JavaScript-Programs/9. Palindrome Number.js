/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let ref = 0;
    let temp = x;
    while(x > 0)
    {
        ref = ref*10 + x%10;
        x = Math.floor(x/10);
    }
    if(ref == temp)
    {
        return true;
    }
    return false
};