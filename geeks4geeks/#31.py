# question --> https://practice.geeksforgeeks.org/problems/replace-all-0-with-5-in-an-input-integer/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def convertFive(self, n):
        # Code here
        temp = list(str(n))
        for index, char in enumerate(temp):
            if char == '0':
                temp[index] = '5'
        return int(''.join(temp))

    # TC: O(N); SC: O(N)
# end
