class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        problem statement: given non-overlapping intervals, insert a new interval
        into the existing intervals such that intervals is still sorted ascendingly.
        merge overlapping intervals if needed.

        SAME TIME = overlapping

        solution: go interval by interval and compare new interval to each one. three possible states:

        * new interval starts after this interval finishes, add this interval to the result.
        * new interval ends before this interval starts, add newInterval and remaining intervals, return.
        * neither, newInterval overlaps with this interval. set newInterval to the merged interval and continue
        '''
        res = []

        for i in range(len(intervals)):
            # new interval's start is AFTER this interval's finish, add this interval
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # new interval's finish is BEFORE this interval's start, this interval can cleanly be inserted
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                # our interval overlaps, merge with this interval
                # we do not add newInterval after this, as it could overlap with future intervals
                # change newInterval and find place for it in later iterations
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        # if by the end we haven't inserted newInterval, it goes at the end
        res.append(newInterval)
        return res
        
