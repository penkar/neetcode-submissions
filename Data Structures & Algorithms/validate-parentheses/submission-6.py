class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for c in s:
            if c == '[':
                ans.append(']')
            if c == '{':
                ans.append('}')
            if c == '(':
                ans.append(')')

            if c == ')' or c == '}' or c == "]":
                if len(ans) == 0:
                    return False

            if c == ')':
                if ans[-1] == ")":
                    ans.pop()
                else:
                    return False
            if c == ']':
                if ans[-1] == "]":
                    ans.pop()
                else:
                    return False
            if c == '}':
                if ans[-1] == "}":
                    ans.pop()
                else:
                    return False

        if len(ans) != 0:
            return False
        return True