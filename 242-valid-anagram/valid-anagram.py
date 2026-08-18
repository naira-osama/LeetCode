class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss, tt = list(s), list(t)
        ss.sort()
        tt.sort()

        return ss == tt
        