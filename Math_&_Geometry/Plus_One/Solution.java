class Solution {
    boolean check( int[] digits ){
        for( int d : digits ){
            if( d != 9 ) return false ;
        }
        return true ; 
    }
    public int[] plusOne(int[] digits) {
        if( check( digits ) ){
            int[] ans = new int[digits.length+1] ; 
            ans[0] = 1; 
            return ans ; 
        }
        int c = 1 ; 
        for( int i=digits.length-1 ; i>=0 ; --i ){
            int sum = digits[i] + c ; 
            digits[i] = sum % 10 ; 
            c = sum/10 ; 
        }
        return digits ; 
    }
}