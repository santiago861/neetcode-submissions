class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = {}
        t_counts = {}
        for i in range(len(s)):
            s_counts[s[i]] = 1 + s_counts.get(s[i], 0)
            t_counts[t[i]] = 1 + t_counts.get(t[i], 0)
        if s_counts != t_counts:
            return False
        else:
            return True