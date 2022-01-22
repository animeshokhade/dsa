# question --> https://www.hackerrank.com/challenges/nested-list/problem?h_r=profile
# default
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

    # my_code
    stack = list()

    for x in range(int(input())):
        name = input()
        score = float(input())
        stack.append([name, score], )

    second_lowest = lowest = 100.0

    for student in stack:
        if (student[1] <= lowest):
            lowest = student[1]

    for student in stack:
        if (student[1] <= second_lowest and student[1] > lowest):
            second_lowest = student[1]

    sort = list()

    for student in stack:
        if (student[1] == second_lowest):
            sort.append(student[0])

    sort = sorted(sort)
    for x in sort:
        print(x)

# end