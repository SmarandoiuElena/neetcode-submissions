class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest_prefix = ""
        n = len(strs[0])
        for i in range(n):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return longest_prefix
            
            longest_prefix += strs[0][i]

        return longest_prefix