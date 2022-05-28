# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        n = len(intervals)
        ans = []

        # if the end is less than start
        if newInterval.end < newInterval.start:
            newInterval.start, newInterval.end = newInterval.end, newInterval.start

        for i in range(n):
            interval = intervals[i]
            if interval.end < newInterval.start:
                ans.append(interval)
            elif interval.start > newInterval.end:
                ans.append(newInterval)
                for j in range(i, n):
                    ans.append(intervals[j])
                return ans
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
                # else repeats till we arrive at the non-overlapping interval
                # to process it.

        # in case the new interval is at the end
        ans.append(newInterval)
        return ans

# alternate approach

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        N = len(intervals)
        for i in range(N):

            x = intervals[i].start
            y = intervals[i].end

            a = newInterval.start
            b = newInterval.end

            # when newInterval start after current interval add current interval to result
            # (start of newInterval 'a' is greater than end of current interval 'y')
            if y < a:
                res.append(intervals[i])

            # when newInterval end before current interval stop iterating (all interval from i to end will be added after new interval)
            # (end of newInterval 'b' is less than start of current interval 'x')
            elif b < x:
                i = i - 1
                break

            # in case of overlap: update start and end of new interval
            else:
                newInterval.start = min(x, a)
                newInterval.end = max(y, b)

        # interval lesser to new interval already in res - Just add newInterval

        temp = Interval(newInterval.start, newInterval.end)
        res.append(temp)

        # all remaining interval will be added if any
        if len(intervals[i + 1:]) > 0:
            for x in range(i + 1, N):
                res.append(intervals[x])
        return res