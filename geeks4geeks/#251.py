# question --> https://practice.geeksforgeeks.org/problems/unique-numbers3019/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Hash&sortBy=submissions

class Solution:
    def uniqueNumbers(self, L, R):
        # code here
        uni = []
        for num in range(L, R + 1):
            if len(set(str(num))) == len(str(num)):
                uni.append(str(num))

        return uni

    # TC: O(R - L); SC: O(R - L) 