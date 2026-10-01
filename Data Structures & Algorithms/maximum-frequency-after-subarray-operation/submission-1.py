class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums_diff = [k - num for num in nums]
        original_k = nums_diff.count(0)
        zeros = 0
        occurrences = {}
        min_start = {}
        best_gain = 0

        for x in nums_diff:

            if x == 0:

                zeros += 1

                continue

            t = occurrences.get(x, 0) + 1

            start_value = (t - 1) - zeros

            if x not in min_start:

                min_start[x] = start_value

            else:

                min_start[x] = min(min_start[x], start_value)

            gain = (t - zeros) - min_start[x]

            best_gain = max(best_gain, gain)

            occurrences[x] = t

        return original_k + best_gain