class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[0,0]
        h={}
        i=0
        for x in nums:
            if (target-x) in h:
                ans[0]=h[target-x]
                ans[1]=i
            else:
                h[x]=i
            i=i+1
        return ans