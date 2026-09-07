class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]  # Lowest price seen so far (best day to have bought)

        for sell in prices:
            # If we sold today, what's the profit using the cheapest buy seen before?
            maxP = max(maxP, sell - minBuy)

            # Update the cheapest buying opportunity for future days
            minBuy = min(minBuy, sell)

        return maxP  # Best profit found across all sell days