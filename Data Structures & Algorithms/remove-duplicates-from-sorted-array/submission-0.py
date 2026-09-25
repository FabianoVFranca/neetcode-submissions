class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 0
        for i in range(len(nums) -1, 0 ,-1):
            if nums[i] == nums[i -1]:
                duplicates +=1
                second_pointer = i
                while second_pointer < len(nums) - duplicates:
                    temp = nums[second_pointer]
                    nums[second_pointer] =  nums[second_pointer + 1]
                    nums[second_pointer + 1] =  temp
                    second_pointer += 1
                
        while duplicates != 0:
            nums.pop(len(nums)-1)
            duplicates -=1
                
        return len(nums)



        