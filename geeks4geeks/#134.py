# question --> https://practice.geeksforgeeks.org/problems/fascinating-number3751/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:

    def fascinating(self, n):
        # code here
        if n < 100:
            return 0

        fas = str(n) + str(n * 2) + str(n * 3)
        fas_set = set(fas)
        return (len(fas) == 9) and ('0' not in fas_set) and (len(fas) == len(fas_set))

    # TC: O(1); SC: O(1)
