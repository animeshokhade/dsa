def printPat(n):
    # Code here
    pattern = ''
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            for k in range(i, 0, -1):
                pattern += str(j) + ' '
        pattern += '$'
    return pattern

    # TC: O(n * n * i); SC: O(1)
