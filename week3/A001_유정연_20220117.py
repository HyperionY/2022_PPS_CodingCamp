class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        stack =[]
        g.sort()
        s.sort()
        
        while s:
            if not g:
                break
            n = s.pop(0)
            for i in range(len(g)):
                if n >= g[i]:
                    stack.append(g.pop(i))
                    break
        
        return len(stack)
            