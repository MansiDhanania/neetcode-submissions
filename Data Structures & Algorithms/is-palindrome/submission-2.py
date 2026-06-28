class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace("?", "")
        s=s.replace(".", "")
        s=s.replace(" ", "")
        s=s.replace(",", "")
        s=s.replace("'", "")
        s=s.replace(":", "")
        s=s.lower()
        return (True if list(s)==list(s)[::-1] else False)