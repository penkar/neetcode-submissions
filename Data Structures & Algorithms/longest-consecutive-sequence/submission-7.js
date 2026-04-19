class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const obj = new Set(nums);
        nums = nums.map(x => {
            if (!obj.has(x - 1)) return x;
        }).filter(x => x!== undefined);

        nums = nums.map(x => {
            let h = 0;
            while(obj.has(x)) {
                x++;
                h++
            };
            return h;
        });
        return Math.max(...nums, 0);
    }
}
