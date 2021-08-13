class Solution:
    def mySqrt(self, x: int) -> int:
        t=0
        for i in range(0, x//2+2):
            if(x>i*i):
                t=i
                continue
            elif(x==i*i):
                return i
            else:
                return t