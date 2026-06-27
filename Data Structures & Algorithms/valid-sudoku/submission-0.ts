class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board: string[][]): boolean {
        const seen = new Set()
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                const val = board[i][j]
                if (board[i][j] !== '.') {
                    const rowCoord = `row ${i} has ${val}`;
                    const colCoord = `col ${j} has ${val}`;
                    const quadrant = `box ${Math.floor(i / 3)}-${Math.floor(j / 3)} has ${val}`;
                    if (seen.has(rowCoord) || seen.has(colCoord) || seen.has(quadrant)) {
                        return false
                    }

                    seen.add(rowCoord)
                    seen.add(colCoord)
                    seen.add(quadrant)
                }

            }
        }

        return true
    }
}
