def top_k_frequent(L,k):
    # create hash map each elment with his occurence
    map={}
    for elt in L:
        map[elt]=map.get(elt,0)+1
    hash = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
    return list(hash)[:k]

L=[4,1,-1,2,-1,2,3]
print(top_k_frequent(L,2)) # Time complexity of this algorithm is O(nlogn) because of sorting 
# we need an O(n) time complexity solution : i should not try to sort the map by value(frequencies)