class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def solve(self, A, B):
        n = len(A)
        if n < 3:
            return n

        ans = 0

        for i in range(n):
            cor = {}
            cur_max = 0
            dup = 0
            ver = 0

            for j in range(i + 1, n):
                if (
                        A[i] == A[j]
                        and B[i] == B[j]
                ):
                    dup += 1
                elif A[i] == A[j]:
                    ver += 1
                else:
                    x_diff = A[j] - A[i]
                    y_diff = B[j] - B[i]

                    z = self.gcd(x_diff, y_diff)

                    x_diff //= z
                    y_diff //= z

                    if cor.get((x_diff, y_diff)) == None:
                        cor[(x_diff, y_diff)] = 1
                    else:
                        cor[(x_diff, y_diff)] += 1

                    cur_max = max(cur_max, cor[(x_diff, y_diff)])

                # vertical points might be more than the slanted points
                cur_max = max(cur_max, ver)

            ans = max(ans, cur_max + dup + 1)  # 1 for the current(i) element

        return ans

        # TC: O(N^2log(max_cor_diff)); SC: O(N^2)