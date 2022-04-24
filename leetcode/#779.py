# question --> https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base condition 
        
        if n == 1: 
            return 0
        
        # Recursive relation
        
        mid = 1 << (n - 2)
        if k <= mid: 
            return self.kthGrammar(n - 1, k)
        else: 
            return 1 - self.kthGrammar(n - 1, k - mid)
        
        # TC: O(N); SC: O(N)
        
# end 