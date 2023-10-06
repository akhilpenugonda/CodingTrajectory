/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let i = 0;
    let j = height.length-1;
    let water = 0
    while(i < j)
    {
        water = Math.max(water, (j-i)*(Math.min(height[j], height[i])));
        if(height[i] < height[j])
        {
            i++;
        }
        else
        {
            j--;
        }
    }
    return water
};
