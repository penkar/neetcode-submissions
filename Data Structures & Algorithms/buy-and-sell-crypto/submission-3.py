class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice = 0
        m = 0
        # pricearray = [0] * len(prices)
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > maxprice:
                maxprice = prices[i]
            # pricearray[i] = maxprice - prices[i]
            if maxprice - prices[i] > m:
                m = maxprice - prices[i] 
        return m
        # return max(pricearray)