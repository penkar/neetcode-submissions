class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        flag = True
        for c in s:
            if c == '[':
                ans.append(']')
            if c == '{':
                ans.append('}')
            if c == '(':
                ans.append(')')

            if c == ')' or c == '}' or c == "]":
                if len(ans) == 0:
                    flag = False
                    break

            if c == ')':
                if ans[-1] == ")":
                    ans.pop()
                else:
                    flag = False
                    break
            if c == ']':
                if ans[-1] == "]":
                    ans.pop()
                else:
                    flag = False
                    break
            if c == '}':
                if ans[-1] == "}":
                    ans.pop()
                else:
                    flag = False
                    break
        if len(ans) != 0:
            flag = False
        return flag