class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        
        for i in nums1:
            n = nums2.index(i)
            
            if n + 1 >= len(nums2):
                answer.append(-1)
            else:
                exist = False
                for j in nums2[n+1:]:
                    if j > i:
                        answer.append(j)
                        exist = True
                        break
                if not exist:
                    answer.append(-1)
        
        return answer