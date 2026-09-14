class Solution {
    public:
        bool isValidSudoku(vector<vector<char>>& board) {
            vector< vector<bool> > lines( 9 , vector<bool>( 10 , false ) ) ;
            vector< vector<bool> > cols( 9 , vector<bool>( 10 , false ) ) ;
            vector< vector<bool> > block( 9 , vector<bool>( 10 , false ) ) ;
            for( int i=0 ; i<9 ; ++i ){
                for( int j=0 ; j<9 ; ++j ){
                    if( board[i][j] != '.' ){
                        int num = board[i][j] - '0' ; 
                        if( lines[i][num] || cols[j][num] ){
                            return false ; 
                        }else {
                            lines[i][num] = true ; 
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
    };