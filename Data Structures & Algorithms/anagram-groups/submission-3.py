class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashtable = defaultdict(list)
        for string in strs:
            frequency = [0] * 26
            for c in string:
                frequency[ord(c) - ord('a')] += 1
            hashtable[tuple(frequency)].append(string)

        return list(hashtable.values())