class Solution {
    int getNext( int n ){
            int next = 0 ; 
            while( n > 0 ){
                int r = n%10 ; 
                next += r*r ; 
                n /= 10 ; 
            }
            return next ;
    }
    public boolean isHappy(int n) {
        if( n == 1 ) return true ; 
        int slow = n , fast = n ; 
        while( true ){
            fast = getNext( getNext(fast) ) ; 
            slow = getNext(slow) ; 
            if( fast == 1 ) return true; 
            if( slow == fast ) return false ; 
        }
    }
}