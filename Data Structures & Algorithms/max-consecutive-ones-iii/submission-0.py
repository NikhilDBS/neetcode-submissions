class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        left = 0
        for right, n in enumerate(nums):
            if n == 0:
                k-=1
            while(k<0):
                if nums[left]==0:
                    k+=1
                left+=1
            longest = max(longest, (right-left)+1)
        return longest