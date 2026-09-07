class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        StringS, StringT = {},{}

        for i in range(len(s)):
            StringS[s[i]] = 1 + StringS.get(s[i], 0)
            StringT[t[i]] = 1 + StringT.get(t[i], 0)
        
        
        return StringS == StringT
        