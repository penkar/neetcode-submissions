class Solution:
    def trap(self, height: List[int]) -> int:
        prefixArray = [0] * len(height);
        suffixArray = [0] * len(height);
        for i in range(len(height)):
            if i == 0:
                prefixArray[0] = height[0]
                suffixArray[-1] = height[-1]
            else:
                prefixArray[i] = max(prefixArray[i - 1], height[i])
                suffixArray[len(height) - i - 1] = max(suffixArray[len(height) - i], height[len(height) - 1 - i])

        total = 0
        for i in range(len(height)):
            total += min(prefixArray[i], suffixArray[i]) - height[i]

        return total
