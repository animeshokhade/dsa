# question --> https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        ans = [[0 for r in range(rows)] for c in range(cols)]
        for c in range(cols):
            for r in range(rows):
                ans[c][r] = matrix[r][c] 
        return ans  
        
        # TC: O(R*C); SC: O(R*C)
        
# Editorial

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
        
# end
