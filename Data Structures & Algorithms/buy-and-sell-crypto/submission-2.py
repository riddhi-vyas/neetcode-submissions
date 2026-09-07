# Time comp: O(n), Space comp: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = float('-inf')
        min_buy = float('inf')
        for i in range(len(prices)):
            min_buy = min(min_buy, prices[i])
            max_profit = max(max_profit, (prices[i]-min_buy))
        return max_profit