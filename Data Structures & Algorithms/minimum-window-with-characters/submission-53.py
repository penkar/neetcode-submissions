class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        counts = {}
        for c in t:
            counts[c] = 1 + counts.get(c, 0)
            # targets[c] = 0
        

        def check(counts, targets, l, r) -> bool:
            for c in counts:
                if counts[c] > targets.get(c, 0):
                    return False
            return True

        res = ""
        l, r = 0, 0
        while r < len(s) and l < len(s):
            targets = {}
            rc = s[r]
            lc = s[l]
            for c in s[l:r + 1]:
                targets[c] = targets.get(c, 0) + 1
            print(21, 'l', l, lc, 'r', r, rc, targets, counts, res, s[l:r + 1])

            if check(counts, targets, l, r):
                if res == "" or len(res) > r - l + 1:
                    res = s[l:r+1]

            if lc in counts and targets[lc] > counts[lc]:
                l += 1
                continue

            if l < r and lc not in counts:
                l += 1
                continue

            if r == len(s) - 1:
                l += 1
                continue

            r += 1
        return res
            






