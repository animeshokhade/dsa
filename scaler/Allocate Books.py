class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        ans = -1

        n = len(A)

        # can't allocate N books to B students if -
        if B > n: return ans

        low = max(A)
        high = sum(A)
        while low <= high:
            mid = (low + high) // 2
            if self.check(mid, A, B, n):
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans

    def check(self, mid, A, B, n):
        pages = 0
        student = 1
        for book in A:
            pages += book
            if pages > mid:
                pages = book
                student += 1

        return student > B
        # True
        # Each student has been allocated lower
        # number of pages, and thus we need to increase the
        # page count.
        # low = mid + 1

        # False
        # Each student has been allocated higher number
        # of books than is needed. So, store ans and
        # reduce high.
        # high = mid - 1

        # Range (R) = sum(A) - max(A) + 1
        # TC: O(NlogR); SC: O(1)
