class Solution {
    public:
        vector<int> plusOne(vector<int>& digits) {
            int c = 1 ; 
            for( int i=digits.size()-1 ; i>=0 ;--i ){
                int sum = digits[i] + c; 
                digits[i] = sum % 10 ; 
                c = sum / 10 ; 
            }
            if( c == 1 ){
                digits.insert( digits.begin() , 1 ); 
            }
            return digits ; 
        }
    };