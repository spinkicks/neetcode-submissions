class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            # 1. Count character frequencies (a-z)
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord('a')] += 1

            # 2. Convert list to an immutable tuple to use as the hash key
            key = tuple(count)

            # 3. Group into dictionary
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key].append(s)

        # 4. Return all grouped values directly
        return list(dic.values())