class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.backtrack(0, 0, [], res, candidates, target)
        return res
    def backtrack(self, val, i, curr, res, candidates, target):
        if val == target:
            res.append(list(curr))
            return
        if i >= len(candidates) or val > target:
            return
        curr.append(candidates[i])
        self.backtrack(val + candidates[i], i + 1, curr, res, candidates, target)
        curr.pop()
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        self.backtrack(val, i + 1, curr, res, candidates, target)