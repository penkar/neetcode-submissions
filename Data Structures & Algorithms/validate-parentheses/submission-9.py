class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        mapping1 = {'[':']','(':')','{':'}'}
        mapping2 = {']':'[',')':'(','}':'{'}
        for c in s:
            if c in mapping1:
                ans.append(mapping1[c])
            if c in mapping2:
                if len(ans) == 0:
                    return False
                if ans[-1] != c:
                    return False
                ans.pop()

        if len(ans) != 0:
            return False

        return True