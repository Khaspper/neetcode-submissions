class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def build(curr):
            if curr >= len(nums):
                return [[]]
            perm = build(curr + 1)
            res = []
            for p in perm:
                for i in range(len(p) + 1):
                    ptemp = p.copy()
                    ptemp.insert(i, nums[curr])
                    res.append(ptemp)
            return res
        return build(0)