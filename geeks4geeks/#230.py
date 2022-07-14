# question --> https://practice.geeksforgeeks.org/problems/stack-designer/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

# _push function to insert elements of array to stack
def _push(arr):
    # return a stack with all elements of arr inserted in it
    return arr


# _pop function to print elements of the stack remove as well
def _pop(stack):
    # print top and pop for each element until it becomes empty
    while stack:
        print(stack.pop(), end=' ')