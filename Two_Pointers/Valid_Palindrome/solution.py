# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         Cleaned="".join(c.lower() for c in s if c.isalnum())
#         return Cleaned==Cleaned[::-1]
        
# Time coplexity : O(n) ,Space Complexity : O(n) we use an extra memory 
# Can we do better , solve it with O(1) wihtout using an extra memory just tow pointers pattern !!


class Solution:
    def isPalindrome(self, s):
        left,right=0,len(s)-1
        while left<right:
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True
