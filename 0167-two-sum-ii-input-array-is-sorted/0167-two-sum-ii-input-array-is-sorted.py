class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        ans=[0,0]
        i=0
        j=len(a)-1
        while(i<j):
            if (a[i]+a[j]==target):
                ans[0]=i+1
                ans[1]=j+1
                return ans
            elif (a[i]+a[j]>target):
                j=j-1
            else:
                i=i+1

        return ans