# question --> https://practice.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1/?page=9&status[]=unsolved&sortBy=submissions#

class Solution:

    # Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        if sizeOfStack & 1:
            s.pop(sizeOfStack // 2)
        else:
            s.pop(sizeOfStack // 2 - 1)
        return s

        # TC: O(N); SC: O(N)