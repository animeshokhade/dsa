# question --> https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1/?page=1&status[]=unsolved&category[]=Arrays&sortBy=submissions

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        Sum = 0
        ans = float('-inf')
        i = 0
        flag = False
        for ele in arr: 
            if ele > 0: 
                flag = True
        if not flag: return max(arr)
        
        while i < len(arr):
            Sum += arr[i]
            if Sum < 0: Sum = 0 
            ans = max(ans, Sum)
            i += 1
        return ans 

        # TC: O(N); SC: O(1)
# end