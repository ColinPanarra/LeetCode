class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        final_prices = [] 
        for i, price in enumerate(prices):
            appended = False
            if i != len(prices):
                for discount in prices[i+1:]:
                    if discount <=price:
                        final_prices.append(price-discount)
                        appended = True
                        break
                if appended == False:
                    final_prices.append(price)
                
        return final_prices
