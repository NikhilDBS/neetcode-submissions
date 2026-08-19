from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prods_left = [1] * n
        prods_right = [1] * n
        
        # Loop 1: Calculate running products from left to right
        running_prod = 1
        for i in range(n):
            running_prod *= nums[i]
            prods_left[i] = running_prod
            
        # Loop 2: Calculate running products from right to left
        running_prod = 1
        for i in range(n - 1, -1, -1):
            running_prod *= nums[i]
            prods_right[i] = running_prod
            
        # Loop 3: Multiply elements to the left and elements to the right
        result = []
        for i in range(n):
            # Left product before index i (1 if at the very beginning)
            left_val = prods_left[i - 1] if i > 0 else 1
            
            # Right product after index i (1 if at the very end)
            right_val = prods_right[i + 1] if i < n - 1 else 1
            
            result.append(left_val * right_val)
            
        return result