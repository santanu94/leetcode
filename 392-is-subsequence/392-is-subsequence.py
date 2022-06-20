class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        pos = 0
        for i in t:
            if pos == len_s:
                return True
            if s[pos] == i:
                pos += 1
        
        if pos == len_s:
            return True
        else:
            return False