# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        max_ = 0
        maxMap = {}
        j = len(prices) - 1
        while j >= 0:
            max_ = max(max_, prices[j])
            maxMap[j] = max_
            j -= 1
        
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, maxMap[i]- prices[i])
        
        return maxProfit