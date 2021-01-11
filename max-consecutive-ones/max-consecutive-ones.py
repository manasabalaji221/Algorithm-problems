class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=nums[0]
        max=0
        x=0
        for i in range(0,len(nums)):
            if(nums[i]==1):
                x=x+1
            else:
                if(max<x):
                    max=x
                x=0
        if(max<x):
            max=x
        if max==0:
            return 0
        return max
