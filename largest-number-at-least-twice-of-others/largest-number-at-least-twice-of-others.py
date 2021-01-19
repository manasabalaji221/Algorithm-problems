class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        print(m)
        c=0
        for i in nums:
            if(i!=m):
                if(2*i<=m):
                    c+=1
        if(c==len(nums)-1):
            return nums.index(m)
        else:
            return -1
        
