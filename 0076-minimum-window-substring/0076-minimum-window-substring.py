class Solution(object):
    def minWindow(self, s, t):
        
        if len(t) > len(s):
            return ""
        
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1
        
        have = 0
        need = len(d)
        window = {}
        
        l = 0
        start = 0
        length = float("inf")
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            if c in d and window[c] == d[c]:
                have += 1

            while have == need:               
                if r - l + 1 < length:
                    length = r - l + 1
                    start = l    
                window[s[l]] -= 1
                
                if s[l] in d and window[s[l]] < d[s[l]]:
                    have -= 1
                l += 1
        
        if length == float("inf"):
            return ""
        
        return s[start:start + length]