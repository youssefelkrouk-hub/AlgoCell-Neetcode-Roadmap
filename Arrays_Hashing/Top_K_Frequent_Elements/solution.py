class Solution(object):
    def topKFrequent(self, nums, k):
        n = len( nums )
        count = { } 
        for i in range( n ) : 
            if ( nums[i] not in count ):    
                count[ nums[i] ] = 0 
            count[ nums[i] ] += 1 

        inter = [ [] for j in range(n+1) ]
    
        for i in count : 
            inter[ count[i] ].append( i )
       
        res = [] 
        for i in range( n , 0 , -1 ) : 
            for  j in inter[i]  : 
                res.append( j ) 
                if( len( res ) == k ) : 
                    return res 

        