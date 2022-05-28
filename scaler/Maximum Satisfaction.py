class Solution:
    # @param A : list of integers
    # @return an integer
    def check(self, temp, A):
        count = 0
        for index in range(len(A)):
            if A[index] & temp == temp: # mask
                count += 1
        if count >= 4:
            return True
        return False

    def solve(self, A):
        ans = 0
        for index in range(32, -1, -1):
            temp = ans | (1 << index)
            if self.check(temp, A):
                ans = temp

        return ans

    