class Solution {
    public:
        const int MAX = INT_MAX ; 
        const int MIN = INT_MIN ; 
        int reverse(int x) {
            int rev = 0; 
            while( x!=0 ){
                int d = x%10 ; 
                x/=10 ; 
                if( rev > MAX/10 || ( rev == MAX/10 && d > MAX%10 ) ){
                    return 0 ; 
                }
                if( rev < MIN/10 || ( rev == MIN/10 && d < MIN%10 ) ){
                    return 0 ; 
                }
                rev = rev*10 + d ; 
            }
            return rev ; 
        }
    };