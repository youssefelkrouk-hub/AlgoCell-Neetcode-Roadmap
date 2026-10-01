import java.util.* ; 

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int n = matrix.length ; 
        int m = matrix[0].length ; 
        List<Integer> rs = new ArrayList<>() ; 
        int top = 0 , bottom = n-1; 
        int left = 0 , right = m-1 ; 
        while( top <= bottom && left <= right ){
            // top traversal
            for( int i=left ; i<=right ; ++i ){
                rs.add( matrix[top][i] ) ; 
            }
            // Left Traversal 
            for( int i=top+1 ; i<bottom ; ++i ){
                rs.add( matrix[i][right] ) ; 
            }
            // Bottom Traversal 
            if( bottom != top ){
                for( int i=right ; i>=left ; --i ){
                    rs.add( matrix[bottom][i] ) ; 
                }
            }
            // Right Traversal 
            if( right != left ){
                for( int i=bottom-1 ; i>top ; --i ){
                    rs.add( matrix[i][left] ) ; 
                }
            }
            left++ ; right--;
            top++  ; bottom-- ; 
        }
        return rs ; 
    }
}