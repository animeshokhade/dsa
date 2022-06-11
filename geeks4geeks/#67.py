class Solution:
    def getMoreAndLess(self, arr, n, x):
        # code here
        gte = 0
        lte = 0
        for ele in arr:
            if ele >= x:
                gte += 1
            if ele <= x:
                lte += 1
        return [lte, gte]

    # TC: O(N); SC: O(1)
