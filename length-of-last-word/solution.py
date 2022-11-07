class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        txt = s.split()
        return len(txt[len(txt)-1])
