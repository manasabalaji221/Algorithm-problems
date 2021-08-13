# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin=[]
        while(head!=None):
            bin.append(head.val)
            head=head.next
            
        print(bin)
        c=0
        out=0
        j=len(bin)-1
        while(j>=0):
            if(bin[j]==1):
                out+=pow(2,c)
            c+=1
            j-=1
            
        return out
            
            