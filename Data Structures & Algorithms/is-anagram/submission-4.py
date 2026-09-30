class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f_string = {}
        s_string = {}
        for i in range (len(s)):
            f_string[s[i]] = 1 + f_string.get(s[i],0)
            s_string[t[i]] = 1 + s_string.get(t[i],0)
        return f_string == s_string

