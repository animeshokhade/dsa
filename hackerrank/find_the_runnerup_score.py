# question --> https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# default
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # my_code
    num = list(arr)
    max_num = second_max = -101
    for test in num:
        if (test >= max_num):
            max_num = test

    for test in num:
        if (second_max <= test < max_num):
            second_max = test

    print(second_max)

# end
