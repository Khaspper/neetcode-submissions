class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        i = 0
        while len(res) != len(matrix) * len(matrix[0]):
            res.append(i)
            i += 1
        print(res)
        return []