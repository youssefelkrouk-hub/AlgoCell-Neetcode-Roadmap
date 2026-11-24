class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        map={}
        for elt in s:
            map[elt]=map.get(elt,0)+1
        
        freq=[[] for i in range(len(s)+1)]
        for i in map:
            for k in range(map[i]):
                freq[map[i]].append(i)
        L=[]
        for i in range(len(freq)-1,0,-1):
            for elt in freq[i]:
                L.append(elt)
        
        return "".join(L)
# Inspired by Top K Frequent Elements (Bucket Sort approach)
# Time Complexity: O(n) — counting takes O(n), and each of the n characters is inserted into and read from the buckets once.
# Space Complexity: O(n) — for the frequency bucket list of size n+1, the output list L, and the hash map (O(k) unique chars).
