# brute force => Memory Limit Exceeded

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        process = [[0] * A for _ in range(A)]
        rows = len(B)
        ans = []
        mod = pow(10, 9) + 7

        for row in range(rows):
            if B[row][0] == 1:
                summ = 0
                for a in range(A):
                    summ += sum(process[a])
                    summ %= mod
                ans.append(summ)

            elif B[row][0] == 2:
                r = B[row][1] - 1
                c = B[row][2] - 1
                process[r][c] = 1 - process[r][c]

            elif B[row][0] == 3:
                r = B[row][1] - 1
                for c in range(A):
                    process[r][c] ^= 1

        return ans
        '''
        TC: O(A^2 * Q)
        SC: O(A^2)
        '''

# optimised

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        mod = 1000000007
        Q = len(B)
        summ = 0
        count1 = [0] * A
        row_flip = [0] * A
        ans = []

        for q in range(Q):
            t = B[q][0]
            r = B[q][1]
            c = B[q][2]
            if t == 1:
                ans.append(summ)

            if t == 2:
                cnt = 0
                # checking for previous occurences of the same querry
                for p in range(q + 1):
                    if B[p][0] == 2 and B[p][1] == r and B[p][2] == c:
                        cnt += 1
                r -= 1
                c -= 1
                cnt += row_flip[r]

                if cnt & 1 == 0:  # even -> current state = 0
                    summ -= 1
                    count1[r] -= 1
                else:  # odd -> current state = 1
                    summ += 1
                    count1[r] += 1

            if t == 3:
                r -= 1
                row_flip[r] += 1

                # All the 1s which will be toggled in this operation
                summ -= count1[r]
                count1[r] = (A - count1[r])

                # All the 0s which will be toggled in this operation
                summ += count1[r]

            summ %= mod

        return ans

        '''
        TC: O(Q^2)
        SC: O(Q + A)
        '''