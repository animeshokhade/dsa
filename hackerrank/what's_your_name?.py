# question --> https://www.hackerrank.com/challenges/whats-your-name/problem?h_r=profile
# default
def print_full_name(first, last):
    # Write your code here

# my_code
print('Hello ', first, ' ', last, '! You just delved into python.', sep='')

# default
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# end