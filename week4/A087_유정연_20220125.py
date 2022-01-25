class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxList = []
        total = 0
        numBox = 0
        
        for i in boxTypes:
            n, s = map(int, i)
            boxList.append([s, n])
        boxList.sort(reverse=True)
        
        for i in boxList:
            s, n = map(int, i)
            truckRest = truckSize - numBox
            
            if truckRest < 1:
                break
            elif truckRest >= n:
                numBox += n
                total += n * s
            else:
                numBox += truckRest
                total += s * truckRest
        
        return total
                