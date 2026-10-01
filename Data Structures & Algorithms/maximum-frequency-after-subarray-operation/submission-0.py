class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ans = nums.count(k)
        for v in range(1, 51):
            if v == k:
                continue
            max_gain = 0
            current_gain = 0
            for x in nums: 
                if x == v :
                    current_gain +=1
                elif x == k :
                    current_gain -=1
                
                if current_gain < 0 :
                    current_gain = 0
                if current_gain > max_gain:
                    max_gain = current_gain
            ans = max(ans, nums.count(k) + max_gain)
        return ans