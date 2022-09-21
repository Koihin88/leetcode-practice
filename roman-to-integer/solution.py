class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        
        i = len(s) - 1
        sum = 0
        while(i >= 0):
            num = roman[s[i]]
            sum+=num
            if(i > 0):
                prevNum = roman[s[i-1]]
                if(prevNum < num):
                    sum-=prevNum
                    i-=2
                    continue
            i-=1
            
        return sum
