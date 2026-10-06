class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        total = len(matrix) * len(matrix[0])
        r, c = 0, 0
        loop = 0
        i = 0
        while len(res) < total:
            # Keep going right while c < len(matrix[0]) - loop 
            while c < len(matrix[0]) - loop:
                res.append(matrix[r][c])
                c += 1
            c -= 1
            if len(res) == total: break
            
            # Now go down
            r += 1
            while r < len(matrix) - loop:
                res.append(matrix[r][c])
                r += 1
            r -= 1

            # Now go left
            c -= 1
            while c > -1 + loop:
                res.append(matrix[r][c])
                c -= 1
            c += 1
            loop += 1

            # Now go up
            r -= 1
            while r >= 0 + loop:
                res.append(matrix[r][c])
                r -= 1
            r += 1
            c += 1

        return res