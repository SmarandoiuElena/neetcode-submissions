class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest_prefix = ""
        n = len(strs[0])
        for i in range(n):
            ok = 1
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    ok = 0
            if ok != 0:
                longest_prefix += strs[0][i]
            else:
                break
                
        return longest_prefix