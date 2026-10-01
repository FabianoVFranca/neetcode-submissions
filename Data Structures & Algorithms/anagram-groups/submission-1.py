class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= {}
        for s in strs:
            array = [0] * 26
            for char in s:
                index = ord(char) - ord("a")
                array[index] +=1
            mapping= tuple(array)
            if mapping not in groups :
                groups[mapping] = [s]
            else :
                groups[mapping].append(s)
        
        anwser=[]
        for key in groups:
            anwser.append(groups[key])

        return anwser
        
