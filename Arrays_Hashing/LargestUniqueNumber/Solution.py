def largest_unique_number(L):
    map={}
    for elt in L:
        map[elt]=map.get(elt,0)+1
    result=-1 # if the array has no unique number it should return -1  
    for key,value in map.items():
        if value==1:
            result=max(result,key)
    return result

# time complexity of this algorithm is O(n) , n==len(L)
# space complexity = O(n) because of the use of an extra memory = hash map 