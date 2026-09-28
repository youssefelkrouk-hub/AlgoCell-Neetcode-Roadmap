from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for w in wordDict:
                    if len(w) + i <= n and s[i : i + len(w)] == w:
                        dp[i + len(w)] = True
        return dp[n]
