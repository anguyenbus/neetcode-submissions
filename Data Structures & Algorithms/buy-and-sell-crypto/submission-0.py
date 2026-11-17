class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left, right = 0, 1
        max_profit = 0
        while right < n:
            if prices[left] < prices[right]:
                max_profit = max(prices[right]-prices[left], max_profit)
            else:
                left = right
            right += 1
        return max_profit
        