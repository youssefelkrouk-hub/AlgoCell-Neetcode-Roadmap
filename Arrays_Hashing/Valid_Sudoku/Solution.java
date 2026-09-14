class Solution {
    public boolean valid( char[][] board ){
        boolean[][] rows = new boolean[9][10] ; 
        boolean[][] cols = new boolean[9][10] ; 
        boolean[][] block = new boolean[9][10] ; 
        for( int i=0 ; i<9 ; ++i ){
            for( int j=0 ; j<9 ; ++j ){
                if( board[i][j] != '.' ){
                    int num = board[i][j] -'0' ; 
                    if( rows[i][num] || cols[j][num] ){
                        return false ; 
                    }else {
                        rows[i][num] = true ; 
                        cols[j][num] = true ; 
                    }
                    int in = (i/3)*3 + j/3 ; 
                    if( block[in][num] ){
                        return false ; 
                    }else {
                        block[in][num] = true ; 
                    }
                }
            }
        }
        return true ; 
    }
    public boolean isValidSudoku(char[][] board) {
        if( valid( board )){
            return true ; 
        }
        return false ; 
    }
}