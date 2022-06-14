# question --> https://practice.geeksforgeeks.org/problems/power-of-pow-even-number5440/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

class Solution:
    def sum_of_square_evenNumbers(self, n):
        # Code here
        return int((2 * n * (n + 1) * (2 * n + 1)) / 3)

    # TC: O(1); SC: O(1)
