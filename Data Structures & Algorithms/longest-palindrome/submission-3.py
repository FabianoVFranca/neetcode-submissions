class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_aux = {}
        for char in s:
            if char in hash_aux:
                hash_aux[char] += 1
            else:
                hash_aux[char] = 1
        max_len = 0
        odd_found = 0

        for chave, valor in hash_aux.items():
            if valor % 2 == 0:
                max_len += valor
            else:
                max_len += valor - 1
                odd_found = 1

        return max_len + odd_found