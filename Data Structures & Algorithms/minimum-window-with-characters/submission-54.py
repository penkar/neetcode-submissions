class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        counts = {}
        for c in t:
            counts[c] = 1 + counts.get(c, 0)        

        def check(counts, targets, l, r) -> bool:
            for c in counts:
                if counts[c] > targets.get(c, 0):
                    return False
            return True

        res = ""
        l, r = 0, 0
        while r < len(s) and l < len(s):
            targets = {}
            for c in s[l:r + 1]:
                targets[c] = targets.get(c, 0) + 1

            if check(counts, targets, l, r):
                if res == "" or len(res) > r - l + 1:
                    res = s[l:r+1]

            if s[l] in counts and targets[s[l]] > counts[s[l]]:
                l += 1
                continue

            if l < r and s[l] not in counts:
                l += 1
                continue

            if r == len(s) - 1:
                l += 1
                continue

            r += 1
        return res
            






