class Solution:
    # @param A : list of integers
    # @return an integer
    def merge(self, A, start, mid, end):
        left = start
        center = mid + 1
        sort = []
        pair_count = 0

        while left <= mid and center <= end:
            if A[left] > A[center]:
                pair_count += mid - left + 1
                sort.append(A[center])
                center += 1
            else:
                sort.append(A[left])
                left += 1

        while left <= mid:
            sort.append(A[left])
            left += 1

        while center <= end:
            sort.append(A[center])
            center += 1

        for index in range(len(sort)):
            A[start + index] = sort[index]

        return pair_count

    def mergeSort(self, A, start, end):
        if start == end:
            return 0
        mid = (start + end) // 2
        pair_left = self.mergeSort(A, start, mid)
        pair_right = self.mergeSort(A, mid + 1, end)
        pair_mix = self.merge(A, start, mid, end)
        return pair_left + pair_right + pair_mix

    def solve(self, A):
        return self.mergeSort(A, 0, len(A) - 1) % 1000000007

    '''
    TC: O(NlogN + N) => O(NlogN)
    SC: O(N) 
    '''