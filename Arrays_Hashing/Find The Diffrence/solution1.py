class Solution(object):
    def findTheDifference(self, s, t):
        hash_s={}
        for elt in s:
            hash_s[elt]=hash_s.get(elt,0)+1
        hash_t={}
        for elt in t:
            hash_t[elt]=hash_t.get(elt,0)+1

        for (key,value) in hash_s.items():
            if hash_t[key]==value:
                del hash_t[key]
        for elt in hash_t:
            return elt
        

# deletinh operation in hash map is O(1)

































        

        