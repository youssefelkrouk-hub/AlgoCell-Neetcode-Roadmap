
 public:
      int start, end;
      Interval(int start, int end) {
          this->start = start;
          this->end = end;
}


class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int n = intervals.size() ; 
        int ans = 0 ;
        vector<pair<int,int>> time ; 
        for( auto interval : intervals ){
            time.push_back( { interval.start , 1 } ) ; 
            time.push_back( { interval.end , -1 } ) ; 
        }
        sort( time.begin() , time.end() ) ;
        int curr = 0 ; 
        for( auto t : time ){
            curr += t.second ; 
            ans = max( ans , curr ) ;  
        } 
        return ans ; 
    }
};
