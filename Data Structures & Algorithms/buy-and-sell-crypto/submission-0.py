class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = len(prices)-1
        max_p = 0
        max_r = 0
        for i in range(len(prices)-2,-1,-1):
            max_r = max(max_r,prices[i+1])
            max_p = max(max_p,max_r - prices[i])
        return max_p
            

        