class Solution:
    def maxPower(self, s: str) -> int:
        l=s[0]
        max=0
        x=1
        for i in range(1,len(s)):
            if(s[i]==l):
                print('a')
                l=s[i]
                # if(x!=0):
                x=x+1  
            else:
                l=s[i]
                if(max<x):
                    max=x
                x=1
        if(max<x):
            max=x
        if max==0:
            return 1
        return max
        
