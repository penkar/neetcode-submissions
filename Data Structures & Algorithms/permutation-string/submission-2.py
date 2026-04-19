class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        obj, obj2 = {}, {}
        for c in s1:
            obj[c] = 1 if c not in obj else obj[c] + 1
        for i in range(len(s2)):
            c = s2[i]
            obj2[c] = 1 if c not in obj2 else obj2[c] + 1
            if c not in obj:
                obj[c] = 0
            if i >= len(s1):
                cc = s2[i - len(s1)]
                obj2[cc] = obj2[cc] - 1
            if obj2 == obj:
                return True

        return False