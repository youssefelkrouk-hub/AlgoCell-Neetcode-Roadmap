class KthLargest(object):
    def __init__(self, k, nums):
        self.pq , self.k = nums , k 
        heapq.heapify( self.pq ) 
        while len(self.pq) > k  : 
            heapq.heappop( self.pq )
        
    def add(self, val):
        heapq.heappush( self.pq , val ) 
        if len( self.pq ) > self.k : 
            heapq.heappop( self.pq )
        return self.pq[0]  
        