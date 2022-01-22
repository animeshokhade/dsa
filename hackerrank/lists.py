# question --> https://www.hackerrank.com/challenges/python-lists/problem?h_r=profile
# default
if __name__ == '__main__':
    N = int(input())

    # my_code
    row = list()
    lst = list()
    for i in range(N):
        row = input().split()
        if (row[0] == 'insert'):
            row[1] = int(row[1])
            row[2] = int(row[2])
            lst.insert(row[1], row[2])
        if (row[0] == 'print'):
            print(lst)
        if (row[0] == 'remove'):
            row[1] = int(row[1])
            ind = lst.index(row[1])
            lst.pop(ind)
        if (row[0] == 'append'):
            row[1] = int(row[1])
            lst.append(row[1])
        if (row[0] == 'sort'):
            lst.sort()
        if (row[0] == 'pop'):
            lst.pop()
        if (row[0] == 'reverse'):
            lst.reverse()

# end