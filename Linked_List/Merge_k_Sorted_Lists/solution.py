class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class NodeWrapper : 
    def __init__( self , node ) :
        self.node = node 
    def __lt__( self , other ) :
        return self.node.val < other.node.val 


class Solution(object):
    def mergeKLists(self, lists):
        if( len( lists ) ) == 0 :
            return None
        res = ListNode(0)
        curr = res 
        minHeap = []

        for lst in lists : 
            if lst is not None : 
                heapq.heappush( minHeap , NodeWrapper(lst) )
        
        while minHeap : 
            node_wrapper = heapq.heappop( minHeap )
            curr.next = node_wrapper.node
            curr = curr.next 
        
            if node_wrapper.node.next : 
                heapq.heappush( minHeap , NodeWrapper( node_wrapper.node.next ) )
        return res.next 
        
        