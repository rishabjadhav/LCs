class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # stores all elements that could be the start of a sequence
        starts = []
        hsh = set()

        for n in nums:
            hsh.add(n)
        
        # find starts: n cannot be a start if a n - 1 exists
        # iterate over hsh to prevent iterating over dupes
        for n in hsh:
            if n - 1 in hsh:
                continue
            else:
                starts.append(n)

        globalcount = 0

        # for each start, find successors and create chains
        for s in starts:
            count = 1
            k = s + 1
            while k in hsh:
                count += 1
                k = k + 1
            if count > globalcount:
                globalcount = count
        
        return globalcount
