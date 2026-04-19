class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        a, b = [None] * length, [None] * length
        for i in range(length):
            if i == 0:
                a[i] = nums[i]
                b[length - i - 1] = nums[length - 1 - i]
            else:
                a[i] = nums[i] * a[i - 1]
                b[length - i - 1] = nums[length - 1 - i] * b[length - i]

        ans = [None] * length
        for i in range(length - 1):
            if i == 0:
                ans[0] = b[1]
                ans[length - 1] = a[-2]
            else:
                ans[i] = (a[i-1] * b[i+1])
        return ans


