class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(arr, curr):
            if len(arr) == k:
                res.append(arr.copy())
                return
            if curr > n:
                return
            for i in range(curr, n + 1):
                arr.append(i)
                dfs(arr, i + 1)
                arr.pop()
        dfs([], 1)
        return res