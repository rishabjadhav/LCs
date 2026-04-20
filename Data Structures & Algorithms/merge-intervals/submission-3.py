class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        problem statement: given intervals, merge all overlapping intervals and return an array
        of merged non-overlapping intervals

        solution:

        for each interval, check if it starts after the last interval ended, that's a clear interval, move one

        if the interval started before the last interval ended, there's an overlap. overwrite the last interval we 
        added to have max end time between itself and our interval. move on


        '''

        res = []
        
        intervals.sort(key=lambda x: x[0])

        # holds the last valid interval's finish time
        last = intervals[0][1]
        res.append(intervals[0])

        for i in intervals[1:]:
            # if this interval starts after the last one ended, it's good
            if i[0] > last:
                res.append(i)
                last = i[1]
            else:
                # otherwise, modify the last interval's finish time to merge in this interval
                last = max(res[len(res)-1][1], i[1])
                res[len(res)-1][1] = last
        
        return res
