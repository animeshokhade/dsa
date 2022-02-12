# question --> https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen
# default
def merge_the_tools(string, k):
    # your code goes here

    #my_code
    sub_string = list()
    split = len(string) // k
    count = 0
    for index in range(split):
        sub_string.append(string[count:count + k])
        count += k

    sub_sub_string = list()
    for index, s in enumerate(sub_string):
        sub_sub_string.append(s[0])
        for i in range(1, len(s)):
            if s[i] not in sub_sub_string[index]:
                sub_sub_string[index] += s[i]

    for string in sub_sub_string:
        print(string)

# default
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# end