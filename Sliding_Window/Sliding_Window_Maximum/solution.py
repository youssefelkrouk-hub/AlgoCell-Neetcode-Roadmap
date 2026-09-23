class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len( nums ) 
        rs = [0]*(n-k+1) 
        l = 0 
        deq = deque() 
        for i in range(n) : 
            while deq and nums[deq[-1]] <= nums[i] : 
                deq.pop() 
            deq.append(i)
            while deq[0] < l :
                deq.popleft() 
            if i >= k-1 :
                rs[i-k+1] = nums[ deq[0] ] 
                l += 1 

        return rs 