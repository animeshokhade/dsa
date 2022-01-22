# question --> https://www.hackerrank.com/challenges/python-string-formatting/problem?h_r=profile
# default
def print_formatted(number):
    # your code goes here

    # my_code
    for iteration in range(1, n + 1):
        w = len(str(bin(n))[2:])

        s1 = str(iteration)
        s2 = str(oct(iteration)[2:])
        s3 = str(hex(iteration).upper()[2:])
        s4 = str(bin(iteration)[2:])

        print(s1.rjust(w),
              s2.rjust(w),
              s3.rjust(w),
              s4.rjust(w))

# default
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# end