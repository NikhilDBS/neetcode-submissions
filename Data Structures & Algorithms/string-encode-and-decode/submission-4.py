from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Special marker when input is an empty list []
        if not strs:
            return "#EMPTY#"
        delimiter = "§"
        return delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        # If marker is found, return empty list []
        if s == "#EMPTY#":
            return []
        delimiter = "§"
        return s.split(delimiter)