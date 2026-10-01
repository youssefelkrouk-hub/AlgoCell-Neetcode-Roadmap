package Greedy.Merge_Triplets_to_Form_Target_Triplet;

class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        boolean a = false ; 
        boolean b = false ; 
        boolean c = false ;
        for( int[] t : triplets ){
            if( t[0] == target[0] && t[1] <= target[1] && t[2] <= target[2] ){
                a = true ; 
            }
            if( t[1] == target[1] && t[0] <= target[0] && t[2] <= target[2] ){
                b = true ; 
            } 
            if( t[2] == target[2] && t[1] <= target[1] && t[0] <= target[0] ){
                c = true ; 
            }
            if( a&&b&&c ) return true ; 
        } 
        return false ; 
    }
}