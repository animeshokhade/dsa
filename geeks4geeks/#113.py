# question --> https://practice.geeksforgeeks.org/problems/12-hour-clock-subtraction1708/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def subClock(self, num1, num2):
        # code here
        diff = num1 - num2
        if diff >= 0:
            return diff % 12
        return (diff + 12) % 12

    # TC: O(1); SC: O(1)