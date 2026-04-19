class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset = set()
        for i in nums:
            if i in newset:
                return True
            else:
                newset.add(i);
        return False