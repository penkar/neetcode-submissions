class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        tmp = []
        for i, t in enumerate(temperatures):
            while tmp and tmp[-1][1] < t:
                [j,k] = tmp.pop()
                res[j] = i - j
            tmp.append([i, t])
        return res