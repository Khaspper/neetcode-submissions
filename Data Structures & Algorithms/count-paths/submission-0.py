class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.count = 0
        # [down, right]
        directions = [(0, 1), (1, 0)]

        def dfs(x, y):
            # Check if x and y are in bounds
            if min(x, y) < 0 or x >= n or y >= m :
                return
            if x == n - 1 and y == m - 1:
                self.count += 1
                return
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        dfs(0, 0)
        return self.count