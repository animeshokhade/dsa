# question --> https://www.hackerrank.com/challenges/python-mutations/problem?h_r=profile
# default
def mutate_string(string, position, character):

    # my_code
    return s[:int(i)] + c + s[int(i) + 1:]

# default
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# end