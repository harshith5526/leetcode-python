class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        for i in range(n):
            if needle in haystack:
                return 0
            else:
                return -1
        
