class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] not in s_map:
                if t[i] in t_map:
                    return False
                s_map[s[i]] = t[i]
                t_map[t[i]] = s[i]
            else:
                if s_map[s[i]] != t[i]:
                    return False
        
        return True