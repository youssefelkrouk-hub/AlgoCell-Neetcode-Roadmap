class Solution(object):
    def insert(self, intervals, inter):
        res = [] 
        n = len(intervals)
        for i in range(n) : 
            if inter[0] > intervals[i][1] : 
                res.append( intervals[i] )
            elif inter[1] < intervals[i][0] :
                res.append(inter) 
                res += intervals[i:]
                return res 
            else :
                inter = [ 
                    min( inter[0] , intervals[i][0]) , 
                    max( inter[1] , intervals[i][1] )
                ]
        res.append( inter )
        return res 