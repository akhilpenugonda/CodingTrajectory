/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let visited = new Set();

    while(!visited.has(n))
    {
        visited.add(n);
        n = sumOfSquares(n);
        if(n == 1){
            return true;
        }
    }
    return false;
};

var sumOfSquares = function(n){
    let sum = 0;
    while(n > 0)
    {
        sum += (n%10)*(n%10);
        n = Math.floor(n/10);
    }
    return sum;
}