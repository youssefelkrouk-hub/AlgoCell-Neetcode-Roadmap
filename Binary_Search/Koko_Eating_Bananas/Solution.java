package Binary_Search.Koko_Eating_Bananas;

class Solution {
    public boolean check( int[] piles , int h , int tar ){
        int time = 0 ; 
        for( int i=0 ; i<piles.length ; ++i ){
            time += ( ( piles[i] + tar -1 ) /tar ) ; 
        }
        return time <= h ; 
    }
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1 ; 
        int r = 1_000_000_007 ; 
        while( l < r ){
            int mid = l + ( r - l )/2 ; 
            if( check( piles , h , mid ) ){
                r = mid ; 
            }else {
                l = mid + 1 ; 
            }
        }
        return l ; 
    }
}