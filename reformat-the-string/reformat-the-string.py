class Solution:
    def reformat(self, s: str) -> str:
        a=[]
        d=[]
        out=""
        for i in s:
            if(i>='a' and i<='z'):
                a.append(i)
            else:
                d.append(i)
        print(a,d)
        if(abs(len(a)-len(d))>1):
            return ""
        else:
            print("hgjgu")
            if(len(d)>len(a)):
                for i in range(0,len(d)):
                    if(i<len(d)):
                        print('v',d[i])
                        out+=d[i]
                    if(i<len(a)):
                        out+=a[i]
            else:
                for i in range(0,len(a)):
                    if(i<len(a)):
                        out+=a[i]
                    if(i<len(d)):
                        out+=d[i]
        return out
