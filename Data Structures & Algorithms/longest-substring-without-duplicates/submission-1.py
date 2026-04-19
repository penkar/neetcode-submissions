class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        ttl = 0
        l = 0
        r = 0
        while r < len(s):
            c = s[r]
            if c in charset:
                charset.remove(s[l])
                l += 1
            else:
                charset.add(s[r])
                r += 1
            ttl = max(ttl, r - l)

        return ttl