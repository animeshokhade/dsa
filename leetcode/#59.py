# question --> https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for r in range(n)] for c in range(n)]
        r = c = 0
        s = 1 
        dirc = 1 
        while s <= n * n:
            ans[r][c] = s
            s += 1
            if dirc == 1:
                c += 1
                if c == n or ans[r][c] != 0:
                    dirc = 2
                    c -= 1
                    r += 1
            elif dirc == 2:
                r += 1
                if r == n or ans[r][c] != 0:
                    dirc = 3
                    r -= 1
                    c -= 1
            elif dirc == 3:
                c -= 1
                if c < 0 or ans[r][c] != 0:
                    dirc = 4
                    c += 1
                    r -= 1
            elif dirc == 4:
                r -= 1
                if r < 0 or ans[r][c] != 0:
                    dirc = 1
                    r += 1
                    c += 1
        return ans 
        
        #TC: O(N^2); SC: O(N^2)
        
# end 