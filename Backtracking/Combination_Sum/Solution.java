import java.util.* ; 

class Solution {
    List<List<Integer>> rs; 
    public void backtrack(int val, int[] candidates, int i, List<Integer> curr, int target) {
        if (val == target) {
            rs.add(new ArrayList<>(curr));
            return;
        }
        for( int j=i ; j<candidates.length ; ++j ){
            if( val + candidates[j] <= target ){
                curr.add( candidates[j] ) ; 
                backtrack( val + candidates[j] , candidates , j , curr , target ) ; 
                curr.remove( curr.size() - 1 ) ; 
            }
        } 
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        this.rs = new ArrayList<>();
        backtrack(0, candidates, 0, new ArrayList<>(), target);
        return rs;
    }
}
