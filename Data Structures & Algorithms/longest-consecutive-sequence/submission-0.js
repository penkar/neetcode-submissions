class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const obj = new Set(nums);
        nums = nums.map(x => {
            if (!obj.has(x - 1)) {
                console.log('push', x)
                return x;
            }
            return undefined;
        }).filter(x => x!== undefined);

        let h = 0;

        // console.log({nums, obj})
        nums.forEach(x => {
            let hh = 0;
            while(obj.has(x)) {
                x++;
                hh++
                // console.log({x, hh})
            };
            if (h < hh) h = hh;
            // console.log({hh});
        });
        return h;
    }
}
