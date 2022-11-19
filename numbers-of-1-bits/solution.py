class Solution:
    def hammingWeight(self, n: int) -> int:
        number = str(n)
        count = 0
        for i in range(len(number)):
            if number[i] == '1':
                count += 1
        return count
