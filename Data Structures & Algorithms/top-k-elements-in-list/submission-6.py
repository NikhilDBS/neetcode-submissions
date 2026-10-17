class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        res=[]
        freq = [ [] for i in range (len(nums)+1)]
        for n in nums:
            hmap[n] = 1 + hmap.get(n,0)
        for key,v in hmap.items():
            freq[v].append(key)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res