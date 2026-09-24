package Backtracking.Permutations;

import java.util.* ;

class Solution {
    List<List<Integer>> rs = new ArrayList<>() ;
    public void swap( int[] nums , int i , int j ){
        int temp = nums[i] ; 
        nums[i] = nums[j] ; 
        nums[j] = temp ; 
    }
    public void backtrack( int idx , int[] nums ){
        if( idx == nums.length ){
            List<Integer> perm = new ArrayList<>() ; 
            for( int i : nums ) perm.add(i) ;  
            rs.add( perm ) ; 
            return ; 
        }
        for( int i=idx ; i<nums.length ; ++i ){
            swap( nums , i , idx  ) ; 
            backtrack( idx+1 , nums ) ; 
            swap( nums , i , idx ) ; 
        }
    }
    public List<List<Integer>> permute(int[] nums) { 
        backtrack( 0 , nums ) ;
        return rs ; 
    }
}