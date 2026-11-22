# my idea is to use for each string a hash map 
# each hashmap contain key=chrachters , values = occurence 
# traverse dict of ransomNote and check existence of each charachter with it's occurence  in dict2


def canConstruct(ransomNote, magazine):
    dict1={}
    dict2={}


    for elt in ransomNote:
        dict1[elt]=dict1.get(elt,0)+1
    for elt in magazine:
        dict2[elt]=dict2.get(elt,0)+1
    

    for key,value in dict1.items():
        if key not in dict2:
            return False
        else: # if it's exist in dict2 then check it's occurence 
            if dict2[key]<value:
                return False
    return True


print(canConstruct("aa","aab"))

# time complexity is : O(n+m) n length og ransomNote , m length of magazine