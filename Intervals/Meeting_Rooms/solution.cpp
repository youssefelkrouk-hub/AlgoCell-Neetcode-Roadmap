/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

 class Solution {
    public:
        bool canAttendMeetings(vector<Interval>& intervals) {
            int n = intervals.size() ;
            sort( intervals.begin() , intervals.end() , []( const Interval &a , const Interval &b ){
                return a.start < b.start ; 
            } ) ; 
            for( int i=1 ; i<n ; ++i ){
                if( intervals[i-1].end > intervals[i].start ){
                    return false ; 
                }
            }
            return true ; 
        }
    };
    