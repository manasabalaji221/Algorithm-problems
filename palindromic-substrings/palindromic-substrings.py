class Solution:
    def countSubstrings(self, s: str) -> int:
        subs=[]
        out=[]
        for i in range(len(s)):
            for l in range(i+1,len(s)+1):
                subs.append(s[i: l])
        # print(subs)
        
        for i in subs:
            if(i==i[::-1]):
                out.append(i)
                
        # print(out)
        return len(out)
        
            