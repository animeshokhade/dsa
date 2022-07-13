# question --> https://practice.geeksforgeeks.org/problems/sort-a-string2943/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=accuracy#

class Solution:
    def sort(self, s):
        # code here
        s = list(s)
        for ind, ch in enumerate(s):
            s[ind] = ord(ch)

        s.sort()

        for ind, ele in enumerate(s):
            s[ind] = chr(ele)

        return ''.join(s)

        # TC: O(|s|log|s|); SC: O(1)
