# question --> https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1/?page=1&difficulty[]=0&category[]=Arrays&sortBy=submissions#

class Solution:
    def MissingNumber(self, array, n):
        # my code
        
        summ = (n * (n + 1)) // 2
        
        return summ - sum(array)
        
        # TC: O(N); SC: O(1)
        
# end