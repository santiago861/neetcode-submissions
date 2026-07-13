class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_length = len(s1)
        w1, w2 = 0, 0 + (window_length - 1)
        s1_counts = {}

        for i in s1:
            s1_counts[i] = 1 + s1_counts.get(i, 0)
        
        while w2 < len(s2):
            window_counts = {}
            for k in range(w1, w2+1):
                window_counts[s2[k]] = 1 + window_counts.get(s2[k], 0)
            if window_counts == s1_counts:
                return True
            w1, w2 = w1+1, w2+1
        return False