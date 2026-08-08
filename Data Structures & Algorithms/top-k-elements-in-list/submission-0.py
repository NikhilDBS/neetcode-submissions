from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dict (frequency map) of each number in the list
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Sort the unique numbers based on their frequency in descending order
        sorted_nums = sorted(count.keys(), key=lambda num: count[num], reverse=True)
        
        # Return the top k numbers
        return sorted_nums[:k]