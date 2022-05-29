# question --> https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1/?page=1&status[]=unsolved&sortBy=submissions#

class Solution:
    def majorityElement(self, A, N):
        # Your code here
        if N == 1: return A[0]
        count = 1
        majority = A[0]
        for index in range(1, N):
            if A[index] == majority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count = 1
                    majority = A[index]
        count = 0
        for ele in A:
            if ele == majority:
                count += 1

        if count > N // 2:
            return majority
        return -1
