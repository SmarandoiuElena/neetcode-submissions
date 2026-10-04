class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hastable = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):

            if s[i] in hastable:
                hastable[s[i]] += 1
            else:
                hastable[s[i]] = 1

            if t[i] in hastable:
                hastable[t[i]] -= 1
            else:
                hastable[t[i]] = -1

        for i, j in hastable.items():
            if j != 0:
                return False
        return True
            
        
        