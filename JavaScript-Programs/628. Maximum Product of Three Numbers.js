function maximumProduct(nums) {
    nums.sort((a, b) => a - b);

    const n = nums.length;
    const maxProduct1 = nums[n - 1] * nums[n - 2] * nums[n - 3];
    const maxProduct2 = nums[n - 1] * nums[0] * nums[1];

    return Math.max(maxProduct1, maxProduct2);
}
