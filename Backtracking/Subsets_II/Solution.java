package Backtracking.Subsets_II;

import java.util.*;

class Solution {
    List<List<Integer>> rs = new ArrayList<>() ; 
    int n ; 
    public void backtrack( int idx , int[] nums , List<Integer> curr ){
        rs.add( new ArrayList<>(curr) ) ; 
        for( int i=idx ; i<n ; ++i ){
            if( i > idx && nums[i-1] == nums[i] ) continue ; 
            curr.add( nums[i] ) ; 
            backtrack( i+1 , nums , curr ) ; 
            curr.remove( curr.size() - 1 ) ; 
        }
    }
    public List<List<Integer>> subsetsWithDup(int[] nums) {                    
        this.n = nums.length ; 
        Arrays.sort( nums ) ; 
        backtrack( 0 , nums , new ArrayList<>() ) ; 
        return rs ; 
    }
}