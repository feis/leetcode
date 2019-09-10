# 771. Jewels and Stones
# Use collections.Counter() and sum()
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        m = collections.Counter(S)
        return sum(m[j] for j in J)
