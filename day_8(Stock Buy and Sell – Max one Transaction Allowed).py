class Solution:
    def maximumProfit(self, prices):        # code here
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if min_price > price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit        
        
