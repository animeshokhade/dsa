class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dic = {}
        ans = 0
        mod = pow(10, 9) + 7

        # dictionary
        for ind, ele in enumerate(A):
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1

        for ele in A:
            if B - ele in dic:
                # i != j
                dic[ele] -= 1

                # if the pair constitutes the same element
                # then the frequency must at least be 2
                # to constitute a pair.
                if B - ele == ele and dic[ele] > 1:  # duplicates
                    ans += dic[ele] % mod
                else:
                    ans += dic[B - ele] % mod

                    # restoring the current element
                dic[ele] += 1

        return (ans // 2) % mod

        # TC: O(N); SC: O(N)


# optimisation

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        p1 = 0
        p2 = n - 1
        mod = pow(10, 9) + 7
        ans = 0
        while p1 < p2:
            summ = A[p1] + A[p2]
            if summ < B:
                p1 += 1
            elif summ > B:
                p2 -= 1
            else:
                if A[p1] == A[p2]:
                    # this is a scenario when we encounter duplicates
                    # thus, there are no other elements between p1 and p2 now
                    x = p2 - p1 + 1
                    ans += ((x * (x - 1)) // 2) % mod  # xC2
                    break
                else:
                    dup1 = 1
                    p1 += 1
                    while A[p1] == A[p1 - 1]:
                        p1 += 1
                        dup1 += 1

                    dup2 = 1
                    p2 -= 1
                    while A[p2] == A[p2 + 1]:
                        p2 -= 1
                        dup2 += 1

                    ans += (dup1 * dup2) % mod

        return ans % mod

        # TC: O(N); SC: O(1)
