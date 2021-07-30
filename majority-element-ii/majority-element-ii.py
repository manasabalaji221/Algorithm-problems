class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        out=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d.keys():
            if(d[i]>len(nums)//3):
                out.append(i)
                
        return out