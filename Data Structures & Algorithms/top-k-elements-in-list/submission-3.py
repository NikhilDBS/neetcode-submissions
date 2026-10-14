class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for n in nums:
            hmap[n] = 1 + hmap.get(n,0)
        hmap=sorted(hmap, key=lambda x: hmap[x])
        return hmap[-k:]