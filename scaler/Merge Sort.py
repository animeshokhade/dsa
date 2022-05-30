class Solution:
    # @param A : list of integers
    # @return a list of integers
    def merge(self, A, start, end):
        temp = []
        tstart = start
        mid = (start + end) // 2
        tmid = mid
        mid += 1
        while start <= tmid and mid <= end:
            if A[start] <= A[mid]:
                temp.append(A[start])
                start += 1
            else:
                temp.append(A[mid])
                mid += 1

        # if A[start:mid] is non empty
        while start <= tmid:
            temp.append(A[start])
            start += 1

        # if A[mid + 1:] is non empty
        while mid <= end:
            temp.append(A[mid])
            mid += 1

        # copying the temp array into the A index block
        for index in range(tstart, end + 1):
            A[index] = temp[index - tstart]

        return

    def divideAndConquer(self, A, start, end):
        if start == end:
            return
        mid = (start + end) // 2
        self.divideAndConquer(A, start, mid)  # left branch
        self.divideAndConquer(A, mid + 1, end)  # right branch
        self.merge(A, start, end)
        return A

    def solve(self, A):
        return self.divideAndConquer(A, 0, len(A) - 1)

# best approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def merge(self, A, start, mid, end):
        temp = [0] * (end - start + 1)
        left, right = start, mid + 1
        filler = 0

        while left <= mid and right <= end:
            if A[left] <= A[right]:
                temp[filler] = A[left]
                left += 1
                filler += 1
            else:
                temp[filler] = A[right]
                right += 1
                filler += 1

        # if A[left:mid] is non empty
        while left <= mid:
            temp[filler] = A[left]
            filler += 1
            left += 1

        # if A[mid + 1:] is non empty
        while right <= end:
            temp[filler] = A[right]
            right += 1
            filler += 1

        # copying the temp array into the A index block
        for index in range(end - start + 1):
            A[start + index] = temp[index]

    def divideAndConquer(self, A, start, end):
        if start == end:
            return
        mid = (start + end) // 2
        self.divideAndConquer(A, start, mid)  # left branch
        self.divideAndConquer(A, mid + 1, end)  # right branch
        self.merge(A, start, mid, end)

    def solve(self, A):
        self.divideAndConquer(A, 0, len(A) - 1)
        return A

# TC: O(NlogN); SC: O(N + logN) approx. O(N) [Recursion Stack + temp array merge]
# TC: O(NlogN); SC: O(N)


