class Solution {
    public:
        bool isValid(string s) {
            stack<char> st  ; 
            map<char,char> m ; 
            m[')'] = '(' ; 
            m['}'] = '{' ; 
            m[']'] = '[' ; 
            for( char c : s ){
                if( m.count( c ) ){
                    if( !st.empty() && st.top() == m[c] ){
                        st.pop() ; 
                    }else {
                        return false ; 
                    }
                }else {
                    st.push( c ) ; 
                }
            }
            return st.empty() ; 
        }
    };