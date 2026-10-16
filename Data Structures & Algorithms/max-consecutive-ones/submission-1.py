class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        longest = 0
        one = -1
        for right,n in enumerate(nums):
            if n ==1 :
                one = right+1
                longest = max(longest, (right-left)+1)
            else:
                left = right +1
        return longest