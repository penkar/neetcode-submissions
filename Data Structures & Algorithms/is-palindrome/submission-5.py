class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a, b = 0, len(s) - 1
        print(s, a-b)
        while b - a > 0:
            print('999', s, s[a], s[b])
            if not s[a].isalnum():
                a += 1
                continue
            if not s[b].isalnum():
                b -= 1
                continue
            if s[a] != s[b]:
                return False
            b -= 1
            a += 1
        return True
