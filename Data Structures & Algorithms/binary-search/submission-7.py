class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) < 3:
            for i, t in enumerate(nums):
                if t == target:
                    return i
        
        while r - l > 1:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            idx = (l + r) // 2
            if nums[idx] == target:
                return idx
            if nums[idx] < target:
                l = idx
            else:
                r = idx


        return -1