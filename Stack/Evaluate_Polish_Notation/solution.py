class Solution(object):
    def evalRPN(self, tokens):
        stack = [ ] 
        for c in tokens : 
            if c == "+" : 
                stack.append( stack.pop() + stack.pop() )
            elif c == "*" : 
                stack.append( stack.pop() * stack.pop() )
            elif c == "-" : 
                b = stack.pop()
                a = stack.pop()
                stack.append( a - b ) 
            elif c == "/" : 
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))
                # 
            else :
                stack.append( int(c) )

        return stack.pop() 
            
        