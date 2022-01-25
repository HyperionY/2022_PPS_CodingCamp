class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack = [i for i in nums if i != val]
        nums.clear()
        for i in stack:
            nums.append(i)
        stack.clear()
        
        return len(nums)