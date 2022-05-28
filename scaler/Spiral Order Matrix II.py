class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        ret = [[0 for x in range(A)] for y in range(A)]

    square = A * A
    direction = 1
    row, col = 0, 0

    for number in range(1, square + 1):
        ret[row][col] = number
        # move right
        if direction == 1:
            col += 1
            if col == A or ret[row][col] != 0:
                direction = 2
                col -= 1
                row += 1

        # move down
        elif direction == 2:
            row += 1
            if row == A or ret[row][col] != 0:
                direction = 3
                row -= 1
                col -= 1


        # move left
        elif direction == 3:
            col -= 1
            if col == -1 or ret[row][col] != 0:
                direction = 4
                col += 1
                row -= 1


        # move up
        elif direction == 4:
            row -= 1
            if row == 0 or ret[row][col] != 0:
                direction = 1
                row += 1
                col += 1

    return ret
