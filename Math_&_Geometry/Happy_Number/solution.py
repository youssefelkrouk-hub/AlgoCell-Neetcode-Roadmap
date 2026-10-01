class Solution:
    def getNext(self, n: int) -> int:
        nx = 0
        while n > 0:
            r = n % 10
            nx += r * r
            n //= 10
        return nx

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        slow, fast = n, n
        while True:
            fast = self.getNext(self.getNext(fast))
            slow = self.getNext(slow)
            if fast == 1:
                return True
            elif slow == fast:
                return False
