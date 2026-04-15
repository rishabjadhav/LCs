class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 
        
        '''
        what to solve: find maximum average of a k-length subarray in nums, and return that mean

        brute force: iterate through the array looking at chunks of size k. find chunk average and keep a
        running maximum. return this running max after iterating through whole array.
        
        BRUTE FORCE SOLUTION:
        runningmean = -10000
        i = 0
        while i + k <= len(nums):
            localmean = 0

            for j in range(k):
                localmean += nums[i + j]
            localmean /= k
            if localmean > runningmean:
                runningmean = localmean
            
            i += 1
        
        return runningmean

        optimal solution: everytime we move on to the next chunk, we are adding the same k - 1 elements to 
        localmean. we should find a way to reuse these values. maybe subtracting the element we've passed and
        adding the new element is better?
        '''

        runningmean = -10000
        localsum = 0

        # init starting window
        for f in range(k):
            localsum += nums[f]

        if k == len(nums):
            return localsum / k
            
        if (localsum / k) > runningmean:
            runningmean = (localsum / k)

        i = k

        while i < len(nums):
            # slide window
            localsum -= nums[i-k]
            localsum += nums[i]

            # check
            if (localsum / k) > runningmean:
                runningmean = (localsum / k)
            i += 1
        
        return runningmean

