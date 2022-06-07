# question --> https://practice.geeksforgeeks.org/problems/find-index4752/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def findIndex (self,a, N, key ):
        #code here.
        if key not in a: return [-1, -1]
        start = a.index(key)
        a = a[::-1]
        end = N - a.index(key) - 1
        return [start, end]

    # TC: O(N); SC: O(1)