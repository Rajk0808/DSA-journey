from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        n = len(prices)
        profit = 0
    
        # Traverse the array
        for i in range(1, n):
            # If the current price is higher than the previous price
            if prices[i] > prices[i - 1]:
                # Add the difference to profit
                profit += prices[i] - prices[i - 1]
    
        return profit
                
