# question --> https://practice.geeksforgeeks.org/problems/power-of-pow-odd-numbers1103/1/?page=4&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def sum_of_square_oddNumbers(self, n):
        # Code here
        return (n * (2 * n + 1) * (2 * n - 1)) // 3

    # TC:O(1); SC: O(1)
