class Solution:
    def encode(self, strs) -> str:
        rs = "" 
        for s in strs : 
            rs += str(len(s)) + "#" + s 
        return rs 

    def decode(self, s: str) :
        res,i=[],0
        while i<len(str):
            j=i
            while str[j]!="#":
                j+=1
            length=int(str[i:j])
            res.append(str[j+1:j+1+length])
            i=j+length
        return res
