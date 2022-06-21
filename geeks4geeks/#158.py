# question --> https://practice.geeksforgeeks.org/problems/intersection-of-two-arrays2404/1/?page=3&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        #code here
        return len(set(a).intersection(b))
        # TC: O(n + m); SC: O(n)