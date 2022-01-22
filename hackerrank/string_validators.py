# question --> https://www.hackerrank.com/challenges/string-validators/problem
# default
if __name__ == '__main__':
    s = input()

    # my_code
    a1 = any(i.isalnum() for i in s)
    a2 = any(i.isalpha() for i in s)
    a3 = any(i.isdigit() for i in s)
    a4 = any(i.islower() for i in s)
    a5 = any(i.isupper() for i in s)

    sol = [a1, a2, a3, a4, a5]
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)

# end