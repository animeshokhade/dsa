# question --> https://www.hackerrank.com/challenges/python-string-split-and-join/problem?h_r=profile
# default
def split_and_join(line):
    # write your code here

    # my_code
    string = line.split(' ')
    join = '-'.join(string)

    return join

# default:
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# end