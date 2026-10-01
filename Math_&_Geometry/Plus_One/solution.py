from typing import List
class Solution:
    def check(self, digits: List[int]) -> bool:
        for i in digits:
            if i != 9:
                return False
        return True

    def plusOne(self, digits: List[int]) -> List[int]:
        if self.check(digits):
            ans = [0] * (len(digits) + 1)
            ans[0] = 1
            return ans
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + c
            digits[i] = s % 10
            c = s // 10
        return digits
