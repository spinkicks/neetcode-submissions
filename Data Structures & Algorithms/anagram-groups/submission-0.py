class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        dic = {}
        for i in range(n):
            key = "".join(sorted(strs[i]))
            if key not in dic:
                dic[key] = [strs[i]]
            else:
                dic[key].append(strs[i])
        result = []
        for key in dic:
            result.append(dic[key])
        return result


        