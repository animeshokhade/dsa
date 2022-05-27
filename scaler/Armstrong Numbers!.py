def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    add = 0
    for num in range(1, N + 1):
        string = str(num)
        for i in string:
            digit = int(i)
            add += digit * digit * digit
        if add == num:
            print(num)
        add = 0
    return 0

if __name__ == '__main__':
    main()

    