class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        hashtable = {}
        for string in strs:

            S = "".join(sorted(string))
            if S in hashtable:
                hashtable[S].append(string)
            else:
                hashtable[S] = []
                hashtable[S].append(string)
        
        for value in hashtable.values():
            result.append(value)
        return result
