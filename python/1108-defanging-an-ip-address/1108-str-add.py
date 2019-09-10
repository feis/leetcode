# 1108. Defanging an IP Address
# Use str.__add__
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ''
        for c in address:
            if c == '.':
                ans += '[.]'
            else:
                ans += c
        return ans 
