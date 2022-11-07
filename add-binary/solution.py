class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        a = a[::-1]
        b = b[::-1] 
        for i in range(max(len(a), len(b))):
            numA = int(a[i]) if i < len(a) else 0
            numB = int(b[i]) if i < len(b) else 0

            sum = numA + numB + carry
            single_digit = str(sum % 2)
            result = single_digit + result
            carry = sum // 2

        if carry:
            result = '1' + result
        return result
