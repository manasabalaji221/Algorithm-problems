class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # x="".join(str(x) for x in nums)
        s=nums[0:n]
        t=nums[n:]
        print(s,t)
        d=[]
        for i in range(0,len(s)):
            d.append(s[i])
            d.append(t[i])
        return d
            
       
