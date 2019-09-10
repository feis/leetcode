# 771. Jewels and Stones
# Use nested loops
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for s in S:
            for j in J:
                if s == j:
                    cnt += 1
                    break
        return cnt 
