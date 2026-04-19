class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        for i in strs:
            lcl = {}
            for j in i:
                lcl[j] = lcl[j] + 1 if j in lcl else 1
            arr.append(lcl)
        for i in range(len(strs)):
            c = arr[i]
            if strs[i] == None:
                arr[i] = None
                continue
            ans = [strs[i]]
            for j in range(i + 1, len(strs)):
                if strs[j] == None:
                    continue
                if arr[j] == arr[i]:
                    ans.append(strs[j])
                    strs[j] = None
            arr[i] = ans
        return [x for x in arr if x is not None]