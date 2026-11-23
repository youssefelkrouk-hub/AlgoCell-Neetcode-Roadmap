def top_k_frequent(nums,K):
    map={}
    for elt in nums:
        map[elt]=map.get(elt,0)+1

    freq=[[] for i in range(len(nums)+1)]
    for number,index in map.items():
        freq[index].append(number)
    top_k_frquent=[]
    for i in range(len(freq)-1,0,-1):
        for elt in freq[i]:
            top_k_frquent.append(elt)
            if len(top_k_frquent)==K:
                return top_k_frquent

print(top_k_frequent([4,1,-1,2,-1,2,3],2))




