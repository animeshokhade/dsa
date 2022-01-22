# question --> https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=profile
# default
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # my_code
    marks = student_marks.get(query_name)
    add = 0.00
    for x in marks:
        add += x

    avg = (add / (len(marks)))
    format_avg = '{:.2f}'.format(avg)
    print(format_avg)

# end