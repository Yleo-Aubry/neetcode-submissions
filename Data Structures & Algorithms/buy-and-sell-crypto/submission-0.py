class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=0
        while l < len(prices)-1:
            sell_window=prices[l+1:]
            profit=max(profit,max(sell_window)-prices[l])
            l+=1
        return profit 