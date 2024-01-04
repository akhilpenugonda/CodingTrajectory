class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        minimum = prices[0]
        maximum = 0
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                if prices[i] - minimum > maximum:
                    maximum = prices[i] - minimum
        return maximum
