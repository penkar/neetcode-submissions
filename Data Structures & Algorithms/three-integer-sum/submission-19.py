class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def twoSum(self, l:int, target: int):
            r = len(nums) - 1
            while r != l:
                if nums[l] + nums[r] == target:
                    if [target * -1, nums[l], nums[r]] not in ans:
                        ans.append([target * -1, nums[l], nums[r]])
                if nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            return None


        nums = sorted(nums)
        for i in range(len(nums) - 2):
            a = twoSum(self, i + 1, nums[i] * -1)
        return ans
        