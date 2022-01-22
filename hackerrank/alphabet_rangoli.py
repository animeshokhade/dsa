# question --> https://www.hackerrank.com/challenges/alphabet-rangoli/problem?h_r=profile
# default
def print_rangoli(size):
    # your code goes here

    # my_code
    width = 4 * n - 3
    string = 'abcdefghijklmnopqrstuvwxyz'
    for index in range(-n + 1, n):
        if (abs(index) < n):
            forward = string[abs(index) + 1:n]
            backward = forward[::-1]
            sliced_string = backward + string[abs(index)] + forward
            final_string = '-'.join(sliced_string)
            print(final_string.center(width, '-'))
        else:
            print(string[abs(index)].center(width, '-'))

# default
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# end