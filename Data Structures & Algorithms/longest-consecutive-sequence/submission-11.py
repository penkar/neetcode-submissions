class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set1 = set()
        longest = 1
        for i in nums:
            set1.add(i)
        for i in nums:
            j = i + 1
            while j in set1:
                longest = max(longest, j - i + 1)
                j += 1
        return longest