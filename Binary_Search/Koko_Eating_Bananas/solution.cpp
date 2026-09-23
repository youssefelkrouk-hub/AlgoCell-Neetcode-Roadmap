class Solution {
    public:
        bool check( vector<int>&piles ,int h , int tar ){
            int time = 0 ; 
            for( int i : piles ){
                time += ( i + tar-1 )/tar ; 
            }
            return time <= h ; 
        }
        int minEatingSpeed(vector<int>& piles, int h) {
            int n = piles.size() ; 
            int l = 1 ; 
            int r = 1e9 ; 
            while( l < r ){
                int mid = l + ( r - l )/2 ; 
                if( check( piles , h  ,mid ) ){
                    r = mid ; 
                }else {
                    l = mid + 1 ; 
                }
            }
            return l ; 
        }
    };