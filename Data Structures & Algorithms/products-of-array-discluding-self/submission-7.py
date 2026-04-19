class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # len(nums) = len(nums)
        a, b = [None] * len(nums), [None] * len(nums)
        a[0] = nums[0]
        b[len(nums) - 1] = nums[-1]
        for i in range(1, len(nums)):
            a[i] = nums[i] * a[i - 1]
            b[len(nums) - i - 1] = nums[len(nums) - 1 - i] * b[len(nums) - i]

        ans = [None] * len(nums)
        ans[0] = b[1]
        ans[len(nums) - 1] = a[-2]
        for i in range(1, len(nums) - 1):
            ans[i] = (a[i-1] * b[i+1])
        return ans


