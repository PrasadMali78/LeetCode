class Solution:
    def reverseString(self, s: List[str]) -> None:
       i=0
       j=len(s)-1
       while(i<j):
        c=s[i]
        s[i]=s[j]
        s[j]=c
        i=i+1
        j=j-1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1