class Solution:

    def encode(self, strs: List[str]) -> str:

        string = ""
        for s in strs:
            string += str(len(s))
            string += '#'
            string += s
        return string

    def decode(self, s: str) -> List[str]:
        
        nr = 0
        n = len(s)
        result = []
        i = 0
        while i < n:
            number = ""
            while s[i] != '#':
                number += s[i]
                i += 1
            nr = int(number)
            i += 1
            word = ""
            for j in range(i, i + nr):
                word += s[j]
                i += 1
            result.append(word)

        return result