#Time comp: O(n), n is length of prices
#Space comp: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        #profit = sell_price - buy_price
        min_buy = float('inf')
        start = 0
        for end in range(len(prices)):
            min_buy = min(min_buy, prices[end])
            max_profit = max(max_profit, prices[end]-min_buy)
        return max_profit