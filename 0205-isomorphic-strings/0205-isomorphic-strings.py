class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1=list(s)
        t1=list(t)
        h={}
        for i in range(len(s)):
            if s1[i] in  h and h[s1[i]]!=t1[i]:
                return False
            elif s1[i] not in h and t1[i] in h.values():
                return False
            else:
                h[s1[i]]=t1[i]
        return True