class Solution(object):
    def findTheDifference(self, s, t):
        count={}
        for elt in t:
            count[elt]=count.get(elt,0)+1
        for c in s:
            count[c]-=1
            if count[c]==0:
                del count[c]
        for diff in count:
            return diff
        
        



































        

        