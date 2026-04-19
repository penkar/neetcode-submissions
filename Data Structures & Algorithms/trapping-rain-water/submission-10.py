class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height);
        prefixArray = [0] * l
        suffixArray = [0] * l
        for i in range(l):
            if i == 0:
                prefixArray[0] = height[0]
                suffixArray[-1] = height[-1]
            else:
                prefixArray[i] = max(prefixArray[i - 1], height[i])
                suffixArray[l - i - 1] = max(suffixArray[l - i], height[l - 1 - i])

        total = 0
        for i in range(l):
            total += min(prefixArray[i], suffixArray[i]) - height[i]
        print('prefixArray', prefixArray)
        print('suffixArray', suffixArray)
        print('height', height)


        return total
