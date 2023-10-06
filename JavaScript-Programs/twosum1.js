/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let visitedDict = {};
    for(let i = 0; i < nums.length; i++)
    {
        if((target - nums[i]) in visitedDict)
        {
            return [visitedDict[target - nums[i]], i];
        }
        else
        {
            visitedDict[nums[i]] = i;
        }
    }
};
