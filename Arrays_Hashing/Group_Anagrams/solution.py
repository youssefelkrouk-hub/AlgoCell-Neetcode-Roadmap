# Intuition:
# The intuition is to group words that are anagrams of each other together. 
# Anagrams are words that have the same characters but in a different order.
class Solution(object):
    def groupAnagrams(self, strs):
        strMap = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))

            if s not in strMap:
                strMap[s] = [strs[i]]
            else:
                strMap[s].append(strs[i])
        
        return strMap.values()

        