/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    let resp = 0; 
    for (let i of nums) { 
        if (i == 0) {
            return 0;
        } else {
            if (i < 0) {
                resp += 1;
            }
        }
    }
    if (resp % 2 == 0) {
        return 1;
    } else {
        return -1;
    }
};
