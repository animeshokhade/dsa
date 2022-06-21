# question --> https://practice.geeksforgeeks.org/problems/common-elements1132/1/?page=1&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        # your code here
        return sorted(list(set(A).intersection(set(B)).intersection(set(C))))

        # TC: O(NlogN); SC: O(A + B + C) 

