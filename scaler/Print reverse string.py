import sys
sys.setrecursionlimit(10 ** 6)

def printString(string):
    if len(string) == 0:
        return ''
    print(string[-1], end='')
    printString(string[:len(string) - 1])

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    string = input()
    printString(string)
    return 0

if __name__ == '__main__':
    main()

# alternative approach

import sys
sys.setrecursionlimit(10 ** 6)

def reverseString(string):
    n = len(string)
    if n == 0:
        return ''
    return string[n - 1] + reverseString(string[:n - 1])

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    string = input()
    return print(reverseString(string))

if __name__ == '__main__':
    main()

# alternate approach

def reverse(string, start, end):
    if start >= end:
        return ''.join(string)
    string[start], string[end] = string[end], string[start]
    return reverse(string, start + 1, end - 1)

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    string = list(input())
    print(reverse(string, 0, len(string) - 1))
    return

if __name__ == '__main__':
    main()

# alternate approach

def revstr(ar, i, j):
    if i >= j:
        return "".join(ar)
    temp = ar[i]
    ar[i] = ar[j]
    ar[j] = temp

    return revstr(ar, i + 1, j - 1)


def main():
    s = input()
    ar = list(s)
    i = 0
    j = len(s) - 1
    print(revstr(ar, i, j))


if __name__ == '__main__':
    main()



