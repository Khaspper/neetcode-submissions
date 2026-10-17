class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        res = []
        i, j = 0, 0
        turn = 0

        while len(visited) < (len(matrix) * len(matrix[0])):
            # Go Right
            while j < len(matrix[i]) and (i, j) not in visited:
                res.append(matrix[i][j])
                visited.add((i,j))
                j += 1
            j -= 1
            # print(f"turn: {turn} visited_1: {visited}")

            # Go Down
            i += 1
            while i < len(matrix) and (i, j) not in visited:
                res.append(matrix[i][j])
                visited.add((i,j))
                i += 1
            i -= 1
            # print(f"turn: {turn} visited_2: {visited}")

            # Go Left
            j -= 1
            while j > -1 and (i, j) not in visited:
                res.append(matrix[i][j])
                visited.add((i,j))
                j -= 1
            j += 1
            # print(f"turn: {turn} visited_3: {visited}")

            # Go Up
            i -= 1
            while i > 0 and (i, j) not in visited:
                res.append(matrix[i][j])
                visited.add((i,j))
                i -= 1
            i += 1
            j += 1
            # print(f"turn: {turn} visited_4: {visited}")
            # print()
            turn += 1

        return res