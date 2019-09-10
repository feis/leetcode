# 771. Jewels and Stones
# Use a dict
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        m = {}
        for s in S:
            if s in m:
                m[s] += 1
            else:
                m[s] = 1
        cnt = 0                
        for j in J:
            if j in m:
                cnt += m[j]
        return cnt
