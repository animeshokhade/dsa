# question --> https://www.hackerrank.com/challenges/swap-case/problem?h_r=profile
# default
if __name__ == '__main__':
    s = input()

    # my_code
    def swap_case(s):
        s = s.swapcase()
        return s
    
    # default
    result = swap_case(s)
    print(result)

# end