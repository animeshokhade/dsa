# question --> https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def armstrongNumber(ob, n):
        # code here
        ans = 0
        temp = n
        while temp:
            digit = temp % 10
            ans += pow(digit, 3)
            temp //= 10
        if ans == n: return 'Yes'
        return 'No'

    # TC: O(1); SC: O(1)
# end
