class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        first_pointer = 0
        second_pointer = len(filtered) - 1

        while first_pointer < second_pointer:
            if filtered[first_pointer].lower() != filtered[second_pointer].lower(): return False
            first_pointer += 1
            second_pointer -=1
        return True
        