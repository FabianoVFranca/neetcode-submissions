class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap_aux = {}
        for num in nums:
            if num in hashmap_aux:
                hashmap_aux[num] +=1
            else:
                hashmap_aux[num] = 1
        
        returned = None
        for key in hashmap_aux:
            if hashmap_aux[key] > len(nums)/2:
                returned = key
        
        return returned

        