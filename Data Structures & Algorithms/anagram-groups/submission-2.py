from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a new dict
        # defaultdict(list) automatically creates a new empty list for missing keys
        anagram_map = defaultdict(list)
        
        # For each string in array
        for s in strs:
            # Sort it (join is used because sorted() returns a list of characters)
            sorted_s = "".join(sorted(s))
            
            # If it exists in dict, append string as value.
            # If not, create a new key for sorted string (handled automatically by defaultdict)
            anagram_map[sorted_s].append(s)
            
        # Return the grouped values as a list of lists
        return list(anagram_map.values())