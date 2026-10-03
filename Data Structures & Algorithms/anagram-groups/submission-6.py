class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            #count character frequencies
            count = [0] * 26
            for letter in s:
                count[(ord(letter) - ord('a'))] += 1
            #turn the list into a tuple because dic only takes immutable like tuples
            key = tuple(count)

            # add the string to the dic
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key].append(s)
        #result is an array of the arrays from the dic values
        # result = []
        # for key in dic:
        #     result.append(dic[key])
        # return result
        return list(dic.values()) # simpler syntax

