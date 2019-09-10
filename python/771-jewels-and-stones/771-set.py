# 771. Jewels and Stones
# Use set()
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        s = set(J)
        count = 0
        for c in S:
            if c in s:
                count = count + 1
        return count
