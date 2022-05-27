def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    num = int(input())
    i = 2
    count = 0
    while i * i <= num:
        if num % i == 0:
            return print('NO')
        i += 1

    return print('YES')
    return 0


if __name__ == '__main__':
    main()

    # TC: O(sqrtN); SC: O(1)
# end