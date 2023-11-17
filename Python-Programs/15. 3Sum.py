class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l=len(nums)
        res=[]
        for i in range(l-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=l-1
            while(j<k):
                s=nums[i]+nums[j]+nums[k]
                if(s==0):
                    res.append([nums[i],nums[j],nums[k]])
                    while(j<k and nums[j]==nums[j+1]):
                        j+=1
                    while(j<k and nums[k]==nums[k-1]):
                        k-=1
                    j+=1

        return res


#optimized and using two sum method

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=len(nums)
        res=[]
        d={}
        for i in range(l):
            if(target-nums[i] in d):
                res.append([target-nums[i],nums[i]])
            else:
                d[nums[i]]=1
        return res
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l=len(nums)
        res=[]
        for i in range(l-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            d={}
            for j in range(i+1,l):
                if(nums[j] in d):
                    res.append([nums[i],nums[j],nums[d[nums[j]]]])
                else:
                    d[-nums[i]-nums[j]]=j
        return res


   