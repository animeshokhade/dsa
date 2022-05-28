class Solution:
    # @param A : integer
    # @param B : list of integers
     # @return an long
    def solve(self, A, B):
        ans = 0
        lastOne = 0
        last = 0

        for index in range(A):
            if B[index] == 1:
                last = index + 1
            ans += last

        return ans

# alternative approach

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an long
    def solve(self, A, B):
        n = len(B)
        sub_array = (n * (n + 1)) // 2
        if 0 not in B:
            return sub_array
        else:
            consecutive_zeros = 0
            flag = True
            for i in range(n):
                if B[i] == 0:
                    if flag:
                        start = i
                    flag = False
                else:
                    if not flag:
                        end = i
                        consecutive_zeros += ((end - start + 1) * (end - start)) // 2
                    flag = True

            if B[n - 1] == 0:
                end = n
                consecutive_zeros += ((end - start + 1) * (end - start)) // 2

        return sub_array - consecutive_zeros
