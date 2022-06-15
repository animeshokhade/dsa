# question --> https://practice.geeksforgeeks.org/problems/checcheck-if-two-given-circles-touch-each-other5038/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

import math


class Solution:
    def circleTouch(self, X1, Y1, R1, X2, Y2, R2):
        # code here
        dis = math.sqrt((X1 - X2) ** 2 + (Y1 - Y2) ** 2)
        if dis > R1 + R2: return 0
        return 1

        # TC: O(1); SC: O(1)