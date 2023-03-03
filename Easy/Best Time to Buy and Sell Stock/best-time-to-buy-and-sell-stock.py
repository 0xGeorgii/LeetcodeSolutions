class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        profit = 0
        p = 0
        
        for i in range(len(prices)):
            p = prices[i]
            if p < min_price:
                min_price = p
            elif p - min_price > profit:
                profit = p - min_price
                
        return profit
