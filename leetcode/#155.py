# question --> https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = list()
        self.minstack = list()
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0 or val <= self.minstack[-1]:
            self.minstack.append(val)
        
    def pop(self) -> None:
        if len(self.stack) == 0: 
            return 
        temp = self.stack.pop()
        if temp == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minstack) == 0:
            return -1
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# TC: O(N); SC: O(N)

# end 