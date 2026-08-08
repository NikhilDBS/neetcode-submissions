from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count element frequencies
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        # 2. Initialize frequency buckets
        # freq[i] stores numbers that appear 'i' times
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n, c in count.items():
            freq[c].append(n)
            
        # 3. Collect the top k elements from highest frequency to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
        return res