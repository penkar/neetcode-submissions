class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let obj = {}
        nums.forEach(n => {
            obj[n] = (obj[n] || 0) + 1;
        });
        return Object.entries(obj).sort((a,b) => 
            a[1] < b[1] ? 1 : -1
        ).slice(0, k).map(a => Number(a[0]))
    }
}
