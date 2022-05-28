def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    for i in range(n):
		string1 = '*' * n
		space = ' ' * i
		string2 = string1[:n - i]
		ans = string2 + (2 * space) + string2
		print(ans)
	for j in range(n):
		string1 = '*' * (j + 1)
		space = ' ' * (n - 1 - j)
		string2 = string1[:j + 1]
		ans = string2 + (2 * space) + string1
		print(ans)
    return 0

if __name__ == '__main__':
    main()