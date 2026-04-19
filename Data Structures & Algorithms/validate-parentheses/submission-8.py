class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        mapping = {'[':']',']':'[','(':')',')':'(','{':'}','}':'{'}
        for c in s:
            if c in mapping:
                match c:
                    case '[':
                        ans.append(']')
                    case '{':
                        ans.append('}')
                    case '(':
                        ans.append(')')
            if c == ')' or c == '}' or c == "]":
                if len(ans) == 0:
                    return False
                if ans[-1] != c:
                    return False
                ans.pop()

        if len(ans) != 0:
            return False

        return True