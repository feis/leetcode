# 771. Jewels and Stones
# Use collections.Counter()
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        m = collections.Counter(S)
        cnt = 0
        for j in J:
            cnt += m[j]
        return cnt
