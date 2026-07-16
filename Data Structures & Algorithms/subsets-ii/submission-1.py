class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, arr):
            if start >= len(nums):
                res.append(arr.copy())
                return
            arr.append(nums[start])
            dfs(start + 1, arr)
            arr.pop()
            while i < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(start + 1, arr)
        
        dfs(0, [])
        return res