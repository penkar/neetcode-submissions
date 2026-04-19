class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsObj = {}
        for i in range(len(nums)):
            c = nums[i]
            if c not in numsObj:
                numsObj[c] = i
            if target - c in numsObj and numsObj[target - c] != i:
                return [numsObj[target - c], i]
