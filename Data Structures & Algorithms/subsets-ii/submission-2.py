class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def dfs(start, arr):
            if start >= len(nums):
                res.append(arr.copy())
                return
            arr.append(nums[start])
            dfs(start + 1, arr)
            arr.pop()

            while start + 1 < len(nums) and nums[start] == nums[start + 1]:
                start += 1
            dfs(start + 1, arr)
        
        dfs(0, [])
        return res