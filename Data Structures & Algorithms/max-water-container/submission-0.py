class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, v = 0, len(heights) - 1, 0
        while l != r:
            v = max(v, min(heights[l], heights[r]) * (r - l))
            # print('l', l, heights[l], 'r', r, heights[r], 'v', v, max(v, min(heights[l], heights[r]) * (r - l)))
            if heights[l] > heights[r]:
                r = r-1
            else:
                l = l+1
        return v