class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let numsObj = {};
        for (let i = 0; i < nums.length; i++) {
            let c = nums[i]
            numsObj[c] = numsObj[c] ?? i;
            if (numsObj[target - c] !== undefined && numsObj[target - c] !== i) {
                return [numsObj[target - c], i]
            }
        }
    }
}
