/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAscendingSum = function(nums) {
    let maxSum = 0;
    let i = 0;
    N = nums.length;
    while(i < N)
    {
        let summer = nums[i];
        while(i+1 < N && nums[i+1] > nums[i])
        {
            summer+=nums[i+1];
            i++;
        }
        maxSum = Math.max(summer, maxSum);
        i++;
    }
    return maxSum;
};
//Comment 2
