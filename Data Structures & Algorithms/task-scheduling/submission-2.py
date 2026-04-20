from collections import Counter, deque
import heapq
from typing import List
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        problem statement: return the minimum number of CPU intervals needed to complete all tasks in tasks.
            constraint: a task "X" cannot be rescheduled before a gap of n intervals

        brute force: 

        thinking:
        * for each task, create frequency map of tasks

        * put all tasks' frequency in max heap to prioritize most frequent task first.
        * once the task is applied, add new task frequency to a queue, along with a global time that it can be applied next.
        * once task in queue can be applied again by time, add back to max heap
        * continue until max heap is empty

        '''

        # key = task, value = frequency
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        
        # initialize max heap
        maxHeap = [-t for t in freq.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = collections.deque()

        # while the maxHeap has tasks, or the queue has tasks
        while maxHeap or q:
            time += 1

            if maxHeap:
                # pop the most frequent remaining task, add 1 to represent a decrement in frequency
                c = 1 + heapq.heappop(maxHeap)

                # if the frequency isn't 0 yet, add it to queue alongside the cooldown time
                if c < 0:
                    q.append((c, time + n))
            
            # check the queue for head elements whose cooldown time has expired
            while q and q[0][1] <= time:
                # add the cooled-down tasks back to the heap
                heapq.heappush(maxHeap, q.popleft()[0])

        return time