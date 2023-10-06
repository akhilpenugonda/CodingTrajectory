/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    let res = [];
        for (let i = 0; i < nums.length; ++i) {
            let index = Math.abs(nums[i])-1;
            if (nums[index] < 0)
                res.push(Math.abs(index+1));
            nums[index] = -nums[index];
        }
        return res;
    // let resp = [];
    // let dict = {};
    // for(let i = 0; i < nums.length; i++)
    // {
    //     if(nums[i] in dict)
    //     {
    //         resp.push(nums[i]);
    //     }
    //     else
    //     {
    //         dict[nums[i]] = true;
    //     }
    // }
    // console.log(resp, dict);
    // return resp;
};
