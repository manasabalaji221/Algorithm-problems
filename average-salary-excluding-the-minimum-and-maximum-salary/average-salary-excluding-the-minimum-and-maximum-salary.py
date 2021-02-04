class Solution:
    def average(self, salary: List[int]) -> float:
        mx = max(salary)
        mn = min(salary)
        av=0
        for i in salary:
            if(i != mn):
                if(i!=mx):
                    av+=i
        print(av,mn, mx)
        return av/(len(salary)-2)