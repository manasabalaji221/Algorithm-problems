class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        x=0
        y=0
        d={}
        if(len(arr)==1):
            return arr[0]
        for i in arr:
            if(i in d):
                d[i]+=1
                if(d[i]>len(arr)/4):
                    return i
            else:
                d[i]=1
                
        
            
            