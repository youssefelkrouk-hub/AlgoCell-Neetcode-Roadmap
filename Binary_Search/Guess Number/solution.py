class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid) # this an API function that call a result to continue the game
            if result<0:
                right = mid - 1
            elif result>0:
                left = mid + 1
            else:
                return mid