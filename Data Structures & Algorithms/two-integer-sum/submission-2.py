class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap= {}
        output1= -1
        output2 = -1
        anwser=[]

        for i in range(len(nums)):
            hashMap[nums[i]] = i
        
        for i in range(len(nums)):
            result = target - nums[i]
            if result in hashMap and i != hashMap[result]:
                output1 = i
                output2 = hashMap[result]
                break

        if output1 > output2:
            anwser.append(output2)
            anwser.append(output1)
        else:
            anwser.append(output1)
            anwser.append(output2)



        return anwser



        