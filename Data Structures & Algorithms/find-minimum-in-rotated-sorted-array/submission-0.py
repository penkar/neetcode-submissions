class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        l, r = 0, len(nums) - 1

        min_found = nums[-1]
        while l < r:
            mid = l + (r - l) // 2
            if min_found > nums[mid]:
                min_found = nums[mid]
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return min_found

        
        