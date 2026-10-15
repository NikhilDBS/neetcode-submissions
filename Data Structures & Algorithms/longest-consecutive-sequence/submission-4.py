class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        if nums == []:
            return 0
        seq_set = set(nums)
        for num in seq_set:
            if (num-1) not in seq_set: #to find the smallest in a seq
                length = 1 #default seq length
                while (num+length) in seq_set:
                    length += 1
                longest_seq = max (length, longest_seq)
        return longest_seq