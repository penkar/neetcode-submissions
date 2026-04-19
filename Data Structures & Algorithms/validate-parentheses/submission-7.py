class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
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