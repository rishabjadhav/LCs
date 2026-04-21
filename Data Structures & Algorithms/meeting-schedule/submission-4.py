"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        '''
        problem statement: determine if intervals overlap
        solution: sort them by start time, and compare to every interval's start to the prev finish
        '''
        if not intervals:
            return True
            
        intervals.sort(key=lambda y: y.start)
        
        lastEnd = intervals[0].end
        for i in intervals[1:]:
            if i.start < lastEnd:
                return False
            lastEnd = i.end
        return True
