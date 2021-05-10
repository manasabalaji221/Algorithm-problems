class Solution:
    cnt=0
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        s, ans = A[0], 0
        for i in A:
            ans += max(0, s - i)
            s = max(s + 1, i + 1)
        return ans
        
        
#         def increm(val, cnt):
#             ans=[]
#             if(val in s):
#                 val+=1
#                 cnt+=1
#                 # print(cnt)
#                 ans=increm(val, cnt)
#             else:
#                 # print(cnt, val)
#                 s.append(val)
#                 ans=cnt
#                 # print('an',ans)
#             return ans
                
            
#         s=list(set(A))
#         diff = []
#         d= {}
#         ans =0
#         # cnt=0
#         for i in A:
#             if(i not in d):
#                 d[i]=1
#             else:
#                 diff.append(i)
#                 # A.remove(i)
#         # print('d',diff)
        
#         # print(cnt)
#         c=[]
#         for i in diff:
#             cnt=0
#             c.append(increm(i, cnt))
#             # c+=ans
#         print(A, c)
#         ans=0
#         for i in c:
#             ans+=int(i)
#         return ans
            