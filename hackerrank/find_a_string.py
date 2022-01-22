# question --> https://www.hackerrank.com/challenges/find-a-string/problem?h_r=profile
# default
def count_substring(string, sub_string):

    # my_code
    num = 0
    for i in range(len(string)):
        if (string[i] == sub_string[0]):
            s = i
            for j in sub_string:
                if s <= len(string):
                    if s == len(string):
                        break
                    if j == string[s]:
                        s += 1
                        continue

            if s == i + len(sub_string):
                num += 1
    return num

# default
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
    
# end