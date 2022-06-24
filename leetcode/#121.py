# question --> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_right = [0] * n 
        max_right[-1] = 0
        
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], prices[i + 1])
            
        ret = float('-inf')
        
        for j in range(n):
            ret = max(max_right[j] - prices[j], ret)
            
        if ret <= 0: 
            return 0
        
        return ret 
    
        # TC: O(N); SC: O(N)
        
# optimisation 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = prices[-1]
        max_profit = 0
        
        n = len(prices)
        
        for i in range(n - 2, -1, -1):
            max_so_far = max(max_so_far, prices[i + 1])
            max_profit = max(max_profit, max_so_far - prices[i])
            
        return max_profit 
    
        # TC: O(N); SC: O(1)