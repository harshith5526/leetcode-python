class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for ch in s:
            if ch.isalnum():
                new=new+ch.lower()
        rev=new[::-1]
        if new==rev:
            return True
        else:
            return False
