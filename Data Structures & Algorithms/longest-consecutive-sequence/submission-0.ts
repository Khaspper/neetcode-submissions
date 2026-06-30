class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        const mySet = new Set(nums)
        let maxLength = 0

        for (const n of mySet) {
            if (mySet.has(n - 1)) continue
            let totalLength = 0
            let curr = n
            while (mySet.has(curr)) {
                totalLength += 1
                curr += 1
            }
            maxLength = totalLength > maxLength ? totalLength : maxLength
        }

        return maxLength
    }
}
