class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        dic = {}
        dic2 = {}
        for i in range(n):
            dic[s[i]] = dic.get(s[i], 0) + 1
        for i in range(n):
            dic2[t[i]] = dic2.get(t[i], 0) + 1
        return dic == dic2
