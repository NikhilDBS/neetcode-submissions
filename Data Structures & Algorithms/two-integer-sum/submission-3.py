class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hmap = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in hmap:
                return [hmap.get(diff),i]
            hmap[n]=i