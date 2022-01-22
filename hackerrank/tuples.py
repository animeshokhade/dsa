# question --> https://www.hackerrank.com/challenges/python-tuples/submissions/code/251831217
# default
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

    # my_code
    integer_list = tuple(integer_list)
    print(hash(integer_list))

# end