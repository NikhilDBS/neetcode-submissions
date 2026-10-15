class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f_map = {}
        for a in magazine:
            f_map[a] = f_map.get(a,0)+1
        for b in ransomNote:
            if b not in f_map:
                return False
            f_map[b] -= 1
            if f_map[b] == -1:
                return False
        return True
        