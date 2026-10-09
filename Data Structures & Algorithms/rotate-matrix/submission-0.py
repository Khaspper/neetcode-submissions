class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # First we should be Transposing it
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix)):
                # Switch transpose wise
                print(matrix[r][c], matrix[c][r])
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
        for i in range(len(matrix)):
            matrix[i] = reversed(matrix[i])

        # Then we reverse it