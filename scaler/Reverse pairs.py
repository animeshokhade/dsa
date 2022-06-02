class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] > 2 * A[j]:
                    count += 1
        return count

    '''
    TC: O(N^2)
    '''

# optimised

class Solution:
    # @param A : list of integers
    # @return an integer
    def inversePair(self, A, start, mid, end):
        pointer1 = start
        pointer2 = mid + 1
        count = 0
        while pointer1 <= mid:
            while pointer2 <= end and A[pointer1] > A[pointer2] * 2:
                count += mid - pointer1 + 1
                pointer2 += 1
            pointer1 += 1
        return count

    def merge(self, A, start, mid, end):
        left = start
        right = mid + 1
        merge = []

        while left <= mid and right <= end:
            if A[left] > A[right]:
                merge.append(A[right])
                right += 1
            else:
                merge.append(A[left])
                left += 1

        while left <= mid:
            merge.append(A[left])
            left += 1

        while right <= end:
            merge.append(A[right])
            right += 1

        for index in range(len(merge)):
            A[start + index] = merge[index]

    def mergeSort(self, A, start, end):
        if start == end:
            return 0
        mid = (start + end) // 2
        pair_left = self.mergeSort(A, start, mid)
        pair_right = self.mergeSort(A, mid + 1, end)
        pair_both = self.inversePair(A, start, mid, end)
        self.merge(A, start, mid, end)
        return pair_left + pair_right + pair_both

    def solve(self, A):
        return self.mergeSort(A, 0, len(A) - 1)

    '''
    TC: O(NlogN)
    SC: O(N)
    '''

# clean

class Solution:
    # @param A : list of integers
    # @return an integer
    def inversePair(self, A, start, mid, end):
        pointer1 = start
        pointer2 = mid + 1
        count = 0
        while pointer1 <= mid and pointer2 <= end:
            if A[pointer1] > A[pointer2] * 2:
                count += mid - pointer1 + 1
                pointer2 += 1
            else:
                pointer1 += 1
        return count

    def merge(self, A, start, mid, end):
        left = start
        right = mid + 1
        merge = []

        while left <= mid and right <= end:
            if A[left] > A[right]:
                merge.append(A[right])
                right += 1
            else:
                merge.append(A[left])
                left += 1

        while left <= mid:
            merge.append(A[left])
            left += 1

        while right <= end:
            merge.append(A[right])
            right += 1

        for index in range(len(merge)):
            A[start + index] = merge[index]

    def mergeSort(self, A, start, end):
        if start == end:
            return 0
        mid = (start + end) // 2
        pair_left = self.mergeSort(A, start, mid)
        pair_right = self.mergeSort(A, mid + 1, end)
        pair_both = self.inversePair(A, start, mid, end)
        self.merge(A, start, mid, end)
        return pair_left + pair_right + pair_both

    def solve(self, A):
        return self.mergeSort(A, 0, len(A) - 1)

    '''
    TC: O(NlogN)
    SC: O(N)
    '''