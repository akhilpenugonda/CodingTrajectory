/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if(n == 1)
    return true;
    if(n <= 0)
    {
        return false;
    }
    while(n >= 0)
    {
        if(n == 0 || n == 1)
        {
            return true;
        }
        if(n%2 != 0)
        {
            return false;
        }
        n = n/2;
    }
//Comment
    return true;
};
// var isPowerOfTwo = function(n) {
//     if (n <= 0) {
//         return false;
//     }
//     return (n & (n - 1)) === 0;
// };
