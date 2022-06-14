# question --> https://practice.geeksforgeeks.org/problems/combinational-logic1908/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def logicalOperation(self, A, B, C, D, E, F):
        # code here
        return int((not A and B) or (C and D) or (E and not F))

    # TC: O(1); SC: O(1)
