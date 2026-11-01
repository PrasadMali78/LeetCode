class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        head = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[head] = nums[i]
                head = head+1
        return head