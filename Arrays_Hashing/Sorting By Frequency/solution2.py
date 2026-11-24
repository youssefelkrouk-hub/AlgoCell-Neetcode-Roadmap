class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        map={}
        for elt in s:
            map[elt]=map.get(elt,0)+1
        
        map_sorted=sorted(map.items(), key=lambda x: x[1], reverse=True)
        result=[]
        for elt in map_sorted:
            result.append(elt[0]*elt[1])
        return "".join(result)

