class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        new=prices
        for i in range(0,len(prices)):
            for j in range(i+1, len(prices)):
                if(prices[i]>=prices[j]):
                    new[i]=prices[i]-prices[j]
                    break
        print(new)
        return new
