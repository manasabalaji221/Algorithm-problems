class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        d=max(nums)
        nums.remove(d)
        # print(nums)
        f=max(nums)
        return (d-1)*(f-1)
