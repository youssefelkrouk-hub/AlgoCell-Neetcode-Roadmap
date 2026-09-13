class Solution(object):
    def twoSum(self, nums, target):
        m = { } 
        for i in range( len( nums ) ) : 
            diff = target - nums[i]  # this is the complement, that we search in the value's of thehash map
            if diff in m : 
                return [ i , m[diff] ]
            m[ nums[i] ] = i 

        return [] 