# optimal solution  just on loop : 
def canConstruct(ransomNote, magazine):
    dict={}
    for elt in ransomNote:
        dict[elt]=dict.get(elt,0)+1

    for elt in dict:
        if elt in magazine and 0<dict[elt]:
            dict[elt]-=1
        else:
            return False
    return True


print(canConstruct("aa","aab"))
