# question --> https://practice.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1/?page=1&status[]=unsolved&curated[]=8&sortBy=submissions#

class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        #Your code here
        for index, a in enumerate(arr):
            if a == X:
                return index
        return -1

        # TC: O(N); SC: O(1)

# end 