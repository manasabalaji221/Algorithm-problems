class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        subs=[]
        for i in range(len(s)):
            for l in range(i+1,len(s)+1):
                subs.append(s[i: l]);
                
        # print(subs)
        max=0
        d={}
        for i in subs:
            if(i not in d):
                d[i]=1
            else:
                if(len(i)>max):
                    max=len(i)
                    
        return max