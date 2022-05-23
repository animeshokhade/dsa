# question --> https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1/?page=1&status[]=unsolved&category[]=Arrays&sortBy=submissions#

class Solution:
    def subArraySum(self,arr, n, s): 
        #Write your code here
        start, end = 0, 0
        Sum = 0
        while end < n and start <= end: 
            if Sum < s:
                if arr[end] == s: return [end + 1, end + 1]
                Sum += arr[end]
                end += 1
            elif Sum == s: return [start + 1, end]
            else: 
                Sum -= arr[start]
                start += 1
        while start < end: 
            if Sum == s: return [start + 1, end]
            Sum -= arr[start]
            start += 1
        return [-1]

        # TC: O(N); SC: O(1)

# end