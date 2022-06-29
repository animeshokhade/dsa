# question --> https://leetcode.com/problems/check-if-matrix-is-x-matrix/

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                if i == j or i == c - j - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False

        return True

    # TC: O(N^2); SC: O(1) 
