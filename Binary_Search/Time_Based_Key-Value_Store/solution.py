class TimeMap(object):
    def __init__(self):
        self.m = { } 

    def set(self, key, value, timestamp):
        if key in self.m :
            self.m[key].append( [timestamp,value] )
        else :
            self.m[key] = [ [timestamp,value] ]

    def get(self, key, timestamp):
        if not key in self.m :
            return ""
        l = 0 
        r = len( self.m[key] ) - 1
        while l < r : 
            mid = l + ( r - l + 1 )//2 
            if  self.m[key][mid][0] <= timestamp : 
                l = mid 
            else : 
                r = mid - 1
        if self.m[key][l][0] <= timestamp : 
            return self.m[key][l][1] 
        return  ""
        