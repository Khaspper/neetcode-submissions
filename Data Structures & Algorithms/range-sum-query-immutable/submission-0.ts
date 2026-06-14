class NumArray {
    /**
     * @param {number[]} nums
     */
    prefix: number[];

    constructor(nums: number[]) {
        this.prefix = []
        let total = 0
        for (let i = 0; i < nums.length; i++) {
            total = total + nums[i]
            this.prefix.push(total)
        }
    }

    /**
     * @param {number} left
     * @param {number} right
     * @return {number}
     */
    sumRange(left: number, right: number): number {
        const leftNumber = left > 0 ? this.prefix[left - 1] : 0
        const rightNumber = this.prefix[right]

        return rightNumber - leftNumber
    }
}
