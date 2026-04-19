class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        a, b, c = [None] * length, [None] * length, [None] * length
        a[0] = nums[0]
        b[length - 1] = nums[-1]
        for i in range(1, length):
            a[i] = nums[i] * a[i - 1]
            b[length - i - 1] = nums[length - 1 - i] * b[length - i]

        c[0] = b[1]
        c[length - 1] = a[-2]
        for i in range(1, length - 1):
            c[i] = (a[i-1] * b[i+1])
        return c


