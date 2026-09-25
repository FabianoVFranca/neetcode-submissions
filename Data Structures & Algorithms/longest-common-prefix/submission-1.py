class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 : return ""
        x = sorted(strs)
        first = x[0]
        last = x[len(strs) - 1]
        answer = ""

        for i in range(len(first)):
            if first[i] != last[i]: return answer
            answer += first[i]

        return answer
            

        