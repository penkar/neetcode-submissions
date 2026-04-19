class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a, b = [], [None] * len(nums)
        ttl = 1
        for i in nums:
            ttl *= i
            a.append(ttl)

        ttl = 1
        for i in range(len(nums) - 1, -1, -1):
            ttl *= nums[i]
            b[i] = ttl

        ans = []
        
        for i in range(len(nums)):
            if i == 0:
                ans.append(b[1])
            elif i == len(nums) - 1:
                ans.append(a[-2])
            else:
                ans.append(a[i-1] * b[i+1])
        return ans


