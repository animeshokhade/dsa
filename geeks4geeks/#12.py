# question --> https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1/?page=1&difficulty[]=0&status[]=unsolved&category[]=Arrays&category[]=Strings&sortBy=submissions#

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        if min(arr) > k: 
            return 0
        lookup = {}
        ans = 0
        for a in arr: 
            if k - a in lookup:
                ans += lookup[k - a]
            if a in lookup: 
                lookup[a] += 1
            else: 
                lookup[a] = 1
        return ans 

# TC: O(N); SC: O(N)
# end 