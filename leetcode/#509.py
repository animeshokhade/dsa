# question --> https://leetcode.com/problems/fibonacci-number/

class Solution:
    def Fibonacci(self, n: int) -> int: 
        if n == 0: 
            return 0
        elif n == 1: 
            return 1
        else: 
            return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
    def fib(self, n: int) -> int:
        return self.Fibonacci(n)
        
    # TC: O(2^N); SC: O(N)
    
# end