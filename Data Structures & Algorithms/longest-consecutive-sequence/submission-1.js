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

        let h = 0;

        nums.forEach(x => {
            let hh = 0;
            while(obj.has(x)) {
                x++;
                hh++
            };
            if (h < hh) h = hh;
        });
        return h;
    }
}
