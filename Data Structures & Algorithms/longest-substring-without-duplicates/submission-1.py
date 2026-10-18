class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        r = 0
        while (r<len(s)):
            if s[r] not in s[l:r]:
                r+=1
            else:
                l+=1
            res = max (res, r-l)
            #print(f"{s[l:r]}, {res}")
        return res