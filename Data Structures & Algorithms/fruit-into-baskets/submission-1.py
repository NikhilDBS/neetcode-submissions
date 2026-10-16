class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res=0
        hmap = {}
        for r, fruit in enumerate(fruits):
            hmap[fruit] = hmap.get(fruit,0) + 1
            while len(hmap)>2:
                hmap[fruits[l]]-=1
                if hmap[fruits[l]] == 0:
                    hmap.pop(fruits[l])
                l+=1
            res = max(res, r - l + 1)
        return res