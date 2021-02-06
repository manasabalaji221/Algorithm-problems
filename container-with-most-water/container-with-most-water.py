class Solution:
    def maxArea(self, height: List[int]) -> int:
        # p=0
        # for i in range(0,len(height)):
        #     for j in range(0,len(height)):
        #         if(height[i]>=height[j]):
        #             x=(height[j])*(j-i)
        #         else:
        #             x=(height[i])*(j-i)
        #         if(p<x):
        #             p=x
        # return p
        
        p=0
        l=0
        r=len(height)-1
        while(l<r):
            if(height[l]>=height[r]):
                x=(height[r])*(r-l)
                r-=1
            else:
                x=(height[l])*(r-l)
                l+=1
            if(p<x):
                p=x
        return p