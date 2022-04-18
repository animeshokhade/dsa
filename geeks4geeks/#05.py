# question --> https://practice.geeksforgeeks.org/problems/count-odd-even/1/?page=2&difficulty[]=0&category[]=Arrays&sortBy=submissions#

class Solution:
    def countOddEven(self, arr, n):
        # my code
        odd, even = 0, 0
        
        for index, num in enumerate(arr):
            if arr[index] % 2 == 0:
                even += 1
            
            elif arr[index] %2 == 1:
                odd += 1
                
        print(odd, even)
        return
        
        # TC: O(N); SC: O(1) 
        
# end 