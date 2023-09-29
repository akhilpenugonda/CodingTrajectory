/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let p = 1;
    let i = 0;
    for (p = 1; p < nums.length; p++)
    {
        if(nums[i] == 0)
        {
            if(nums[p] != 0)
            {
                [nums[p], nums[i]] = [nums[i], nums[p]];
                i++;
            }   
        }
        else{
            i++;
        }
    }
        return nums;
    }
