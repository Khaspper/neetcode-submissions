class NumMatrix {
    /**
     * @param {number[][]} matrix
     */
    matrix: number[][];
    constructor(matrix: number[][]) {
        const rows: number = matrix.length;
        const cols: number = matrix[0].length;

        this.matrix = Array.from({ length: rows + 1 }, () => Array(cols + 1).fill(0));

        for (let i = 0; i < rows; i++) {
            let prefix: number = 0
            for (let j = 0; j < cols; j++) {
                prefix += matrix[i][j]
                const above = this.matrix[i][j + 1]
                this.matrix[i + 1][j + 1] = prefix + above
            }
        }
    }

    /**
     * @param {number} row1
     * @param {number} col1
     * @param {number} row2
     * @param {number} col2
     * @return {number}
     */
    sumRegion(row1: number, col1: number, row2: number, col2: number): number {
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        const bottomRight = this.matrix[row2][col2];
        const bottomLeft = this.matrix[row2][col1 - 1];
        const topRight = this.matrix[row1 - 1][col2];
        const corner = this.matrix[row1 - 1][col1 - 1];

        return bottomRight - bottomLeft - topRight + corner
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
