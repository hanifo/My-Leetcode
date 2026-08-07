class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = 0
        j = 0
        ans = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1

        return ans