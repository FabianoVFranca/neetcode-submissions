class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size_new_arr = len(nums) * 2
        new_arr = [0] * size_new_arr
        j = len(nums) 

        for i in range(len(nums)):
            new_arr[i] = nums[i]
            new_arr[j] = nums [i]
            j += 1
        
        return new_arr

        