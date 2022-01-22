# question --> https://www.hackerrank.com/challenges/text-wrap/problem?h_r=profile
# default
import textwrap

def wrap(string, max_width):

    # my_code
    for index in range(0, len(string), max_width):
        if (index <= len(string) - max_width):
            print(string[index:index + max_width])
        else:
            return string[index:]

# default
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# end