# 1108. Defanging an IP Address
# Use str.replace()
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
