class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpr=0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if i!=j and i<j:
                    if prices[j]-prices[i]>maxpr:
                        maxpr=prices[j]-prices[i]
        return maxpr