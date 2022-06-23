# question --> https://practice.geeksforgeeks.org/problems/binary-array-sorting-1587115620/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    
    #Function to sort the binary array.
    def binSort(self, A, N): 
        #Your code here
        #No need to print the array
        l, r = 0, 0
        while r < N: 
            if A[r] == 1:
                r += 1
            else: 
                A[l], A[r] = A[r], A[l]
                if l == r: 
                    r += 1
                l += 1
                
        return A
    # TC: O(N); SC: O(1)