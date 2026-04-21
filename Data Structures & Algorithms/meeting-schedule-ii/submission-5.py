"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        problem statement: given a list of intervals, return how many rooms are needed such that every intervals
        can take place in a room.

        brute force: create rooms as lists, check each interval against each room, return number of rooms with atl 1 meeting

        optimal: use a min-heap, with elements representing the latest ending time of a room
        if an interval's start time falls after the soonest avaliable room, book it there
        if not, it won't work for any room, so 
        '''
        
        minhp = [0]
        res = 1

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        for i in intervals:
            # if this interval starts after the soonest avaliable meeting ends, book it!
            if i.start >= minhp[0]:
                # this can be booked in a room!
                heapq.heappop(minhp)
                heapq.heappush(minhp, i.end)

            else:
                # if the room avaliable soonest isn't avaliable, none of the rooms are avaliable, we need one
                heapq.heappush(minhp, i.end)
                res += 1
        
        return res
        


