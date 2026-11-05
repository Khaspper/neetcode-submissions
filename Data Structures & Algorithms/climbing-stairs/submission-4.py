class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0,1]

        for i in range(n):
            res.append(res[i] + res[i + 1])
        
        return res[-1]
