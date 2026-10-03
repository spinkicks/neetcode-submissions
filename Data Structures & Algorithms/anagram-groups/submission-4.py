class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            #count character frequencies
            count = [0] * 26
            for letter in s:
                count[(ord(letter) - ord('a'))] += 1
            
            key = tuple(count)

            if key not in dic:
                dic[key] = [s]
            else:
                dic[key].append(s)
        result = []
        for key in dic:
            result.append(dic[key])

        return result

