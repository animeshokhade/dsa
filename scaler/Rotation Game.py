def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    array = list(map(int, input().split()))
    N = array[0]
    slicedArray = array[1:]
    rotations = int(input())
    rotations %= N
    newArray = slicedArray[-rotations:] + slicedArray[:-rotations]
    for number in newArray:
        print(number, end = ' ')
    return 0

if __name__ == '__main__':
    main()

    