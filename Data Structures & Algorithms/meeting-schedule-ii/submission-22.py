"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # We are doing this as if all S, E points are on a single timelime
        # So we arrange them by ascending order       
        starts = [i.start for i in intervals]
        starts.sort()
        ends = [i.end for i in intervals]
        ends.sort()

        res = count = 0
        s = e = 0
        n = len(intervals)

        while s < n:
            # when a meeting starts, use the room
            if starts[s] < ends[e]:
                s += 1
                count += 1
            # when a meeting ends, empty a room
            else:
                e += 1
                count -= 1
            # answer is max of the running count
            res = max(res, count)
        return res
