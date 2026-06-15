class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const prefix: number[] = [];
        const postfix: number[] = [];

        let mult: number = 1;

        for (const n of nums) {
            prefix.push(mult);
            mult *= n;
        }

        mult = 1;
        for (let i = nums.length - 1; i >= 0; i--) {
            postfix.push(mult)
            mult *= nums[i]
        }
        
        for (let i = 0; i < nums.length; i++) {
            prefix[i] = prefix[i] * postfix[nums.length - 1 - i]
        }

        return prefix
    }
}
