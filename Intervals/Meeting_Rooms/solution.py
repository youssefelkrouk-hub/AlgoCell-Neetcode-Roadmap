class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort( key = lambda p : p.start )
        n = len( intervals )
        for i in range( 1 ,n) :
            if intervals[i-1].end > intervals[i].start : 
                return False 
        return True 