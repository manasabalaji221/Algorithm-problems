class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        out=[]
        if(len(str1)<len(str2)):
            o=1
            x=str1
        else:
            o=0
            x=str2
            
        print(x)
        
        for i in range(1,len(x)+1):
            divi = x[:i]
            print('divi', divi)
            if(len(str1)%len(divi)!=0 or len(str2)%len(divi)!=0):
                continue
            
            a=""
            b=""
            while(a!=str1):
                a+=divi
                if(len(a)>len(str1)):
                    break
            
            while(b!=str2):
                b+=divi
                if(len(b)>len(str2)):
                    break
            print(a,b)
            if(a==str1 and b==str2):
                out.append(divi)
        if(len(out)>0):
            max=0
            m=0
            for i in out:
                if(len(i)>max):
                    max=len(i)
                    m=i
            return m
        else:
            return ""
            
            
#             divi=x[:i]
#             while(len(str1)>0):
#                 if(divi in str1):
#                     str1.replace(divi,"")
#                 else:
#                     return ""


#             while(len(str2)>0):
#                 if(divi in str2):
#                     str2.replace(divi,"")
#                 else:
#                     return ""
                
#             if(str1=="" and str2==""):
#                 return divi
                
                        
                