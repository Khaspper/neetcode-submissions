class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, temp):
            if not nums:
                res.append(temp)
                return
            temp.append(nums[0])
            dfs(nums[1:], temp)
            temp.pop()
            dfs(nums[1:], temp)
        return res