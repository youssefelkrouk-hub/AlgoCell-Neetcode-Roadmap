class Solution(object):
    def isValidSudoku(self, board):
        cols = [ [0]*10 for i in range(9) ] 
        rows = [ [0]*10 for i in range(9) ] 
        block = [ [0]*10 for i in range(9) ] 
        for i in range(9) : 
            for j in range(9) : 
                if board[i][j] == '.' : 
                    continue 
                num = ord( board[i][j] ) - ord( '0' )
                if rows[i][num] == 1 or cols[j][num] == 1 : 
                    return False  
                rows[i][num] = 1 
                cols[j][num] = 1 
                ind = ( i//3)*3 + (j//3) 
                if block[ind][num] == 1 : 
                    return False 
                block[ind][num] = 1
                
        return True 