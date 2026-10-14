class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap= defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            hmap[sorteds].append(s)
        result = []
        for v in hmap:
            result.append(hmap.get(v))
        return result