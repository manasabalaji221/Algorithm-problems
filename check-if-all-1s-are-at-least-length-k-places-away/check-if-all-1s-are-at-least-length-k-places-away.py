class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        x=0
        c=0
        for i in range(0,len(nums)):
            if(nums[i]==1):
                print(i)
                if(c==0):
                    x=i
                    c+=1
                elif(i-x>k):
                    x=i
                    c+=1
                    print(x)
                else:
                    return False
        return True
                
