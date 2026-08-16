class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(c.lower() for c in s if c.isalnum() and c.isascii())
        mid = len(s)//2
        #print(s[-1:mid-1:-1])
        if (len(s)%2==0) & (s[0:mid]==s[-1:mid-1:-1]):
            return True
        elif (len(s)%2>0) & (s[0:mid]==s[-1:mid:-1]):
            return True
        return False