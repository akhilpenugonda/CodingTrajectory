/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let rev = 0;
    let isPositive = false;
    
    if (x > 0) {
        isPositive = true;
    }
    x = Math.abs(x);
    while (x > 0) {
        let rem = x % 10;
        rev = rev * 10 + Math.abs(rem); // Fixed line
        x = Math.floor(x / 10);
    }
    if(rev >= Math.pow(2, 31) || rev < -1*Math.pow(2,31))
    {
        return 0;
    }
    if (isPositive) {
        return rev;
    }
    return -1 * rev;
};
