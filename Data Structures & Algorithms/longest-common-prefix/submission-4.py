class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        rg = len(strs[0])
        result = ""
        for i in range(rg):
            current_letter = strs[0][i]
            for j in range(n):
                if len(strs[j]) < (i+1):
                    return result
                if current_letter != strs[j][i]:
                    return result
            result += current_letter
        return result