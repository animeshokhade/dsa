def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    add = 0
    for num in range(N + 1):
        add += num
    return print(add)

if __name__ == '__main__':
    main()