class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #edge case
        if not prices:
            return 0
        max_profit = float('-inf')
        min_price = float('inf')
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(prices[i]-min_price, max_profit)
        return max_profit
#time comp: O(n)
#space comp: O(1)