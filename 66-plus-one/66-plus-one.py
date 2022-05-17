class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        i =  n - 1
        while carry != 0 and i >= 0:
            digits[i] += carry
            carry = int( digits[i] / 10 )
            digits[i] %= 10
            i -= 1
        return digits if carry == 0 else [1] + digits
        