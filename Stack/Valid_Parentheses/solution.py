class Solution(object):
    def isValid(self, s):
        stack = [] 
        mp = { "}" : "{" , ")" : '(' , "]" : "[" } 
        for c in s : 
            if c in mp : 
                if stack and stack[-1] == mp[c] :
                    stack.pop() 
                else :
                    return False 
            else : 
                stack.append( c )

        return not stack        