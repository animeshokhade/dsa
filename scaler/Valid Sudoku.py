class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):

    # rows

    for index1, string in enumerate(A):
        row = set()
        for index2, char in enumerate(string):
            if char != '.':
                if char in row:
                    return 0
                else:
                    row.add(char)

    # columns

    col, row = 0, 0
    iterations = 9
    while col < iterations:
        col_elements = set()
        row = 0
        while row < iterations:
            if A[row][col] != '.':
                if A[row][col] in col_elements:
                    return 0
                else:
                    col_elements.add(A[row][col])
            row += 1
        col += 1

    # boxes

    box = list()
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            temp = ''
            switch = row
            for _ in range(3):
                temp += A[switch][col:col + 3]
                switch += 1
            box.append(temp)

    for index1, string in enumerate(box):
        boxx = set()
        for index2, char in enumerate(string):
            if char != '.':
                if char in boxx:
                    return 0
                else:
                    boxx.add(char)

    return 1
