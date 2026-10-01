import java.util.* ; 


public class Interval {
      public int start, end;
      public Interval(int start, int end) {
          this.start = start;
          this.end = end;
      }
}


class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        int n = intervals.size() ; 
        int ans = 0 ; 

        List<int[]> time = new ArrayList<>() ; 
        for( Interval inter : intervals ){
            time.add( new int[]{ inter.start , 1 } ) ; 
            time.add( new int[]{ inter.end , -1 } ) ; 
        }
        Collections.sort( time ,  (a,b) ->{
            if( a[0] == b[0] ){
                return a[1] - b[1] ; 
            }
            return a[0] - b[0] ; 
        }) ; 
        
        int curr = 0 ; 
        for( int[] t : time ){
            curr += t[1] ; 
            ans = Math.max( ans , curr ) ; 
        }
        return ans ; 
    }
}
