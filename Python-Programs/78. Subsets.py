class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1. Iterative
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res
        # 2. Recursive
        # if not nums: return [[]]
        # res = self.subsets(nums[:-1])
        # return res + [item + [nums[-1]] for item in res]
        # 3. Bit Manipulation
        # return [[nums[i] for i in range(len(nums)) if mask >> i & 1] for mask in range(2 ** len(nums))]
        # 4. Backtracking
        # res = []
        # def dfs(nums, path, res):
        #     res.append(path)
        #     for i in range(len(nums)):
        #         dfs(nums[i+1:], path+[nums[i]], res)
        # dfs(nums, [], res)
        # return res
        # 5. Iterative
        # res = [[]]
        # for num in nums:
        #     res += [item + [num] for item in res]
        # return res
        # 6. Recursive
        # if not nums: return [[]]
        # res = self.subsets(nums[:-1])
        # return res + [item + [nums[-1]] for item in res]
        # 7. Bit Manipulation
        # return [[nums[i] for i in range(len(nums)) if mask >> i & 1] for mask in range(2 ** len(nums))]
        # 8. Backtracking
        # res = []
        # def dfs(nums, path, res):
        #     res.append(path)
        #     for i in range(len(nums)):
        #         dfs(nums[i+1:], path+[nums[i]], res)
        # dfs(nums, [], res)
        # return res
        # 9. Iterative
        # res = [[]]
        # for num in nums:
        #     res += [item + [num] for item in res]
        # return res
        # 10. Recursive
        # if not nums: return [[]]
        # res = self.subsets(nums[:-1])
        # return res + [item + [nums[-1]] for item in res]
        # 11. Bit Manipulation
        # return [[nums[i] for i in range(len(nums)) if mask >> i & 1] for mask in range(2 ** len(nums))]
        # 12. Backtracking
        # res = []
        # def dfs
        # res.append(path)
        # for i in range(len(nums)):
        #     dfs(nums[i+1:], path+[nums[i]], res)
        # dfs(nums, [], res)
        # return res