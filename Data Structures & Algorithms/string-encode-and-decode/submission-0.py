class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string = encoded_string + str(len(s)) + "#" + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        index = 0
        index2 = 0
        strNum = 0
        result = []
        while(index2) != len(s):
            while s[index2] != "#":
                index2 += 1
            length = int(s[index:index2])
            index2 += 1
            word = (s[index2: index2 + length])
            result.append(word)
            index2 += length
            index = index2
            strNum += 1

        return result
