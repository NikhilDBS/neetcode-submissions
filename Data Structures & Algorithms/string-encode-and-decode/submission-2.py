from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Use a non-ASCII character as the separator delimiter
        delimiter = "§"
        res = ""
        
        for s in strs:
            # Length of string + non-ASCII delimiter + the string itself
            res += str(len(s)) + delimiter + s
            
        return res

    def decode(self, s: str) -> List[str]:
        delimiter = "§"
        res = []
        i = 0
        
        while i < len(s):
            # Find where the delimiter character is located
            j = i
            while s[j] != delimiter:
                j += 1
                
            # Extract the string length prefix
            length = int(s[i:j])
            
            # Extract the string payload using the parsed length
            res.append(s[j + 1 : j + 1 + length])
            
            # Advance index past the delimiter and the extracted string payload
            i = j + 1 + length
            
        return res