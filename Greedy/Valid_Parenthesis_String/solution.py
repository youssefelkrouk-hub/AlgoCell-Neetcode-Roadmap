class Solution(object):
    def checkValidString(self, s):
        low = 0 
        high = 0 
        for c in s : 
            if c == '(' :
                low += 1 
                high += 1
            elif c == ')' : 
                low -= 1 
                high -= 1 
            else : 
                low -= 1 
                high += 1 
            if low < 0 : 
                low = 0 
            if high < 0 : 
                return False 
        return low == 0 
        