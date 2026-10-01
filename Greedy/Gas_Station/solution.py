class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas) 
        fl = 0 
        for i in range( n ) : 
            fl += ( gas[i] - cost[i] )
        if fl < 0 :
            return -1 
        pref = 0 
        curr = 0
        idx = 0 
        for i in range( n ) :
            pref += gas[i] - cost[i]
            if pref < curr : 
                idx = i + 1  
                curr = pref
        return idx