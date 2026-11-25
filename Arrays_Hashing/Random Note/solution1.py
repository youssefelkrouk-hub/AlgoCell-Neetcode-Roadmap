# la methode dict.get(key,default_value) return dict[key] if key is in dict sinon return the default_value:

def canConstruct(ransomNote, magazine):
    dict1,dict2={},{}
    for elt in ransomNote:
        dict1[elt]=dict1.get(elt,0)+1
    for elt in magazine:
        dict2[elt]=dict2.get(elt,0)+1
    for key,value in dict1.items():
        d=dict2.get(key,0)
        if d<value:
            return False
    return True
