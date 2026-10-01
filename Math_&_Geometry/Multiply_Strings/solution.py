class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        rs = [0] * (n + m)
        for i in range(n):
            a = ord(num1[n - 1 - i]) - ord("0")
            for j in range(m):
                b = ord(num2[m - 1 - j]) - ord("0")
                rs[i + j] += a * b

        c = 0
        for i in range(n + m):
            rs[i] += c
            c = rs[i] // 10
            rs[i] %= 10
        l = n + m - 1
        while l > 0 and rs[l] == 0:
            l -= 1
        ans = ""
        while l >= 0:
            ans += str(rs[l])
            l -= 1

        return ans