package Intervals.Meeting_Rooms;
import java.util.* ;  
 
 class Solution {
    public class Interval {
        public int start, end;
        public Interval(int start, int end) {
            this.start = start;
                this.end = end;
            }
    }
    
    public boolean canAttendMeetings(List<Interval> intervals) {
        int n = intervals.size() ; 
        if( n == 1 ) return true ; 
        Collections.sort( intervals , ( a,b ) -> {
            return a.start - b.start ; 
        }); 
        for( int i=1 ; i<n ; ++i ){
            if( intervals.get(i).start < intervals.get(i-1).end ) return false ; 
        }
        return true ; 
    }
}
