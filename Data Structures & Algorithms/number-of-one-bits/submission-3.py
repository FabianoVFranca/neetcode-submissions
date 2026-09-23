class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        counter = 1
        for _ in range(32):
            if n & counter != 0:
                ans +=1
            counter *= 2
        return ans