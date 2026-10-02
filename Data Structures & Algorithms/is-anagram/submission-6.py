class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        nd = {}
        md = {}
        for c in s:
            nd[c] = nd.get(c, 0) + 1
        for c in t:
            md[c] = md.get(c, 0) + 1
        return nd == md