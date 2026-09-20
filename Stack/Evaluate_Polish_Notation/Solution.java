import java.util.Stack;

class Solution {
    public boolean isOper( String s ){
        return s.equals("+") || s.equals( "-" )
            || s.equals("/") || s.equals( "*" ) ;  
    }
    public int evalRPN(String[] tokens) {
        int n = tokens.length ; 
        int rs = 0 ; 
        Stack<Long> stack = new Stack() ; 
        for( int i=0 ; i<n ; ++i ){
            if( isOper( tokens[i] ) ){
                long b = stack.pop() ; 
                long a = stack.pop() ; 
                if( tokens[i].equals( "+" ) ){
                    stack.add( a+b ) ; 
                }else if( tokens[i].equals( "-" ) ){
                    stack.add( a-b ) ; 
                }else if( tokens[i].equals( "*" ) ){
                    stack.add( a*b ) ; 
                }else {
                    stack.add( a/b ) ; 
                }
            }else {
                boolean flag = true ; 
                int in = 0 ; 
                if( tokens[i].charAt(0) == '-' ){
                    in = 1 ; 
                    flag = false ; 
                }
                
                long curr = 0L ; 
                for(  ; in < tokens[i].length() ; ++in ){
                    curr = curr*10 + ( tokens[i].charAt(in) - '0' ) ; 
                }
                stack.add( flag ? curr : -curr ) ; 
            }
        }
        return (int) ( (long) stack.pop() )  ; 
    }
}