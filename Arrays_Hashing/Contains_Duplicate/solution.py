class Solution(object):
    def containsDuplicate(self, nums):
        s = set() 
        for i in range( len( nums ) ) : 
            s.add( nums[i] ) 
        return len( s ) < len( nums ) # set contain only unique values, this is another way to transform a list into a set 
        