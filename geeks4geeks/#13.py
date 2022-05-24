# question --> https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1/?page=1&difficulty[]=0&status[]=unsolved&category[]=Arrays&category[]=Strings&sortBy=submissions#

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        suffixSum = sum(A)
        prefixSum = 0
        for index, a in enumerate(A): 
            suffixSum -= a
            if prefixSum == suffixSum: return index + 1
            prefixSum += a 
        return -1

# TC: O(N); SC: O(1)
# end 