def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    while T > 0:
        N = int(input())
        A = [0] * N
        countOdd = countEven = 0
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
            if A[i] % 2 == 1:
                countOdd += 1
            else:
                countEven += 1
        B, C = [0] * countOdd, [0] * countEven
        printB = printC = 0
        for i in range(N):
            if A[i] % 2 == 1:
                B[printB] = A[i]
                printB += 1
            else:
                C[printC] = A[i]
                printC += 1
        for i in range(countOdd):
            print(B[i], end = " ")
        print()
        for j in range(countEven):
            print(C[j], end = " ")
        print()
        T -= 1
    return 0

if __name__ == '__main__':
    main()

    