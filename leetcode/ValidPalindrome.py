class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ''.join([c for c in s if c.isalnum()])
        p = p.lower()

# two pointers approach
#        r, l = 0, len(p)-1
#
#        while r <= l:
#            if p[r] != p[l]:
#                return False
#            r += 1
#            l -= 1
#        return True

        return p[::-1] == p

        
