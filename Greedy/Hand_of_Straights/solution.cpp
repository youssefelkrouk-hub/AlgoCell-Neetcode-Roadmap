class Solution {
    public:
        bool isNStraightHand(vector<int>& hand, int groupSize) {
            int n = hand.size() ; 
            if( n % groupSize != 0 ){
                return false ; 
            }
            unordered_map<int,int> count  ; 
            for( int num : hand ){
               count[num]++ ; 
            }
            sort( hand.begin() , hand.end() ) ; 
            for( int num : hand ){
                if( count[num] > 0  ){
                    for( int i=num ; i<num+groupSize ; ++i ){
                        if( count[i] == 0 ) return false ; 
                        count[i] -= 1 ; 
                    }
                }
            }
            return true ; 
        }
    };