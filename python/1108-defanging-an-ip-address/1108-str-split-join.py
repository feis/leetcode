# 1108. Defanging an IP Address
# Use str.split() and str.join()
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))

