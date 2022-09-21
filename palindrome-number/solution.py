class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        divider = 1
        while x > divider*10:
            divider*=10
        
        while x:
            left = x // divider
            right = x % 10
            print(left)
            print(right)
            
            if(left != right):
                return False
            
            x = (x%divider) // 10
            divider/=100
        return True
