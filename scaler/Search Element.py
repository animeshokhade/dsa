def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    for iterations in range(T):
        A = list(map(int, input().split()))
        B = int(input())
        if B in A:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()

