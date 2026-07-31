class Solution(object):
    def reverseOnlyLetters(self, s):
        original = list(s)
        l, r = 0, len(s) - 1
        while l <= r:
            if original[l].isalpha():
                if original[r].isalpha():
                    original[l], original[r] = original[r], original[l]
                    l += 1 ; r -= 1
                else:
                    r -= 1
            else:
                l += 1
        return ''.join(original)