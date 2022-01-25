class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        stack = nums1[:m] + nums2
        stack.sort()
        nums1.clear()
        
        for i in stack:
            nums1.append(i)