class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = [i for i in nums]
        nums.clear()
        cuser = -1000
        
        for i in stack:
            if not cuser == i:
                nums.append(i)
                cuser = i

        return len(nums)