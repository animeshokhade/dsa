# question --> https://practice.geeksforgeeks.org/problems/sort-the-string-in-descending-order3542/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Hash&sortBy=submissions#

class Solution:
    def ReverseSort(self, str):
        # code here
        return ''.join(sorted(str, key=lambda x: ord(x), reverse=True))

        # TC: O(NlogN); SC: O(N) 