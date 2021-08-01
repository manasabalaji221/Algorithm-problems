class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=sorted(score, reverse=True)
        print(s)
        ranks=[0]*len(score)
        for i in range(len(score)):
            x=s.index(score[i])
            if(x==0):
                ranks[i]="Gold Medal"
            elif(x==1):
                ranks[i]="Silver Medal"
            elif(x==2):
                ranks[i]="Bronze Medal"
            else:
                ranks[i]=str(x+1)
        return ranks
