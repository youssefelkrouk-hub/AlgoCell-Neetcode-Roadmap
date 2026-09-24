#include <iostream> 
#include <vector> 


using namespace std ; 

class Solution {
public:
    vector<string> curr ;
    bool isPal( string &s , int l , int r ){
        while( l < r ){
            if( s[l] != s[r] ){
                return false ; 
            }
            l++ ; r--; 
        }  
        return true ; 
    }
    void backtrack( vector<vector<string>> &rs , string &s , int in ){
        if( in == s.size() ){
            rs.push_back( curr ) ; 
            return ; 
        }
        for( int i=in ; i<s.size() ; ++i ){
            if( isPal( s , in , i ) ){
                curr.push_back( s.substr( in , i -in + 1 ) ) ; 
                backtrack( rs , s , i+1 ) ; 
                curr.pop_back() ; 
            }
        }
    }
    vector<vector<string>> partition(string s) {
       int n = s.size() ; 
       vector<vector<string>> rs ; 
       backtrack( rs , s , 0 ) ; 
       return rs ; 
    }
};