class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxprice = prices[-1]
        pricearray = [0] * len(prices)
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > maxprice:
                maxprice = prices[i]
            pricearray[i] = maxprice - prices[i]
            
        print('priceArray', pricearray, 'm', maxprice)
        return max(pricearray)