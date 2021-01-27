class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s=[]
        x=0
        s.append(x)
        for i in gain:
            s.append(x+i)
            x=x+i
        print(s)
        return max(s)
