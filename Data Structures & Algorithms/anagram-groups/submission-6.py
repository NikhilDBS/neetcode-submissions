from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for string in strs:
            chars = [0]*26
            for s in string:
                chars[ord(s)-ord('a')]+=1
            anagram_map[tuple(chars)].append(string)
        return list(anagram_map.values())