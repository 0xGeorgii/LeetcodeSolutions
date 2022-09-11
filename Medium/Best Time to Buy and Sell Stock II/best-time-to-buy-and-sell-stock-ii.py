class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = []
        min_price = float('inf')
        i = 0        
        
        for j in range(len(prices)):
            price = prices[i]
            if price < min_price:
                min_price = price
            else:
                max_price = price
                while True:
                    i += 1
                    if i >= len(prices):
                        p = max_price if max_price > price else price
                        res.append(p - min_price)
                        break
                    price = prices[i]
                    if price < max_price:
                        res.append(max_price - min_price)
                        min_price = max_price
                        i -= 1
                        break
                    else:
                        max_price = price            
            
            i += 1
            if i >= len(prices):
                break
                
        return sum(res)
