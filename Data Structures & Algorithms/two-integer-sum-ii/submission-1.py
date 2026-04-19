class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for j in range(len(numbers)):
            i = numbers[j]
            if i + i == target:
                if numbers[j + 1] == i:
                    return [j + 1, j + 2]
            elif target - i in numbers:
                return [j + 1, numbers.index(target - i) + 1]
        