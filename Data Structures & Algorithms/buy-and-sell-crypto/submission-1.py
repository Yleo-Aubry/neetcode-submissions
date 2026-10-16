class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index_buy=0
        profit = 0 
        for i in range(1,len(prices)):
            if prices[i-1]<prices[index_buy]:
                index_buy=i-1
            profit=max(profit,prices[i]-prices[index_buy])
        return profit
            
