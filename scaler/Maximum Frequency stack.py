from collections import deque, Counter
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        stack = deque()
        cnt = Counter()
        ret = []

        for arr in A:
            if arr[0] == 1:
                stack.append(arr[1])
                ret.append(-1)
                cnt[arr[1]] += 1
            else:
                pop_stack = deque()
                lkp = set()
                key = max(cnt, key = lambda x: cnt[x])
                val = cnt.get(key)

                for key, v in cnt.items():
                    if v == val:
                        lkp.add(key)

                while stack and stack[-1] not in lkp:
                    pop_stack.append(stack.pop())

                if stack:
                    p = stack.pop()
                    ret.append(p)
                    cnt[p] -= 1
                    if not cnt[p]:
                        del cnt[p]

                while pop_stack:
                    stack.append(pop_stack.pop())

        return ret

        # TC: O(N^2); SC: O(N)

# optimised

from collections import deque, Counter
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        cnt = Counter()
        stk = {}
        ret = []

        for arr in A:
            if arr[0] == 1:
                cnt[arr[1]] += 1
                if cnt[arr[1]] in stk:
                    stk[cnt[arr[1]]].append(arr[1])
                else:
                    stk[cnt[arr[1]]] = [arr[1]]
                ret.append(-1)
            else:
                f = max(stk)
                if stk[f]:
                    p = stk[f].pop()
                    ret.append(p)
                    cnt[p] -= 1
                    if not cnt[p]:
                        del cnt[p]
                if not stk[f]:
                    del stk[f]

        return ret

        # TC: O(N); SC: O(N) 




