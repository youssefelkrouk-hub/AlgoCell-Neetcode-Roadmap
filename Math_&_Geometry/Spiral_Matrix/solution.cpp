#include <iostream> 
#include <vector> 

using namespace std ; 

class Solution {
    public:
        vector<int> spiralOrder(vector<vector<int>>& matrix) {
            int n = matrix.size() ; 
            int m = matrix[0].size() ; 
            vector<int> rs ; 
            int left = 0 , right = m-1 ; 
            int top = 0 , bottom = n-1 ; 
            while( left <= right && top <= bottom ){
                // Top Traversal
                for( int i=left ; i<=right ; ++i ){
                    rs.push_back( matrix[top][i] ) ; 
                }
                // Left Traversal
                for( int i=top+1 ; i<bottom ; ++i ){
                    rs.push_back( matrix[i][right] ) ; 
                }
                // Bottom Traversal 
                if( top != bottom ){
                    for( int i=right ; i>=left ; --i ){
                        rs.push_back( matrix[bottom][i] ) ; 
                    } 
                }
                //Right Traversal 
                if( left != right ){
                    for( int i=bottom-1 ; i>top ; --i ){
                        rs.push_back( matrix[i][left] ) ; 
                    }
                }
                left++ ; right-- ; 
                top++ ; bottom-- ; 
            } 
            return rs ; 
        }
    };