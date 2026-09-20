package Valid_Parentheses;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>() ; 
        for( char c : s.toCharArray() ){
            if( stack.isEmpty() || c == '(' || c == '[' || c == '{' ){
                stack.add( c ) ; 
            }else if( c == '}' ){
                if( stack.peek() == '{' ){
                    stack.pop() ; 
                }else {
                    return false  ; 
                }
            }else if( c == ')' ){
                if( stack.peek() == '(' ){
                    stack.pop() ; 
                }else {
                    return false  ; 
                }
            }else{
                if( stack.peek() == '[' ){
                    stack.pop() ; 
                }else {
                    return false  ; 
                }
            }

        }
        return stack.isEmpty() ; 
    }
}   