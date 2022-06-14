# question --> https://practice.geeksforgeeks.org/problems/12-hour-clock-addition1206/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def clockSum(self, num1, num2):
        # code here
        return (num1 + num2) % 12

    # TC: O(1); SC: O(1)