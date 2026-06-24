"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:       
        starts = [i.start for i in intervals]
        starts.sort()
        ends = [i.end for i in intervals]
        ends.sort()

        res = count = 0
        s = e = 0
        n = len(intervals)

        while s < n:
            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


