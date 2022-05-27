def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    iteration = int(input())
    numbers = []
    for i in range(iteration):
        numbers.append(int(input()))

    add = 0
    for index, num in enumerate(numbers):
        for x in range(1, num):
            if num % x == 0:
                add += x
        if add == num:
            print('YES')
            add = 0
            continue
        else:
            print('NO')
            add = 0

if __name__ == '__main__':
    main()