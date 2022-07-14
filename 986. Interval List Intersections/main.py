from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        nFirst = len(firstList)
        nSecond = len(secondList)
        result = []
        if nFirst == 0 or nSecond == 0:
            return result
        minVal = firstList[0][0]
        maxVal = firstList[-1][-1]
        
        pFirst = 0
        pSecond = 0
        while pSecond < nSecond and secondList[pSecond][-1] < minVal:
            pSecond += 1
        
        while pFirst < nFirst:
            iStartFirst, iEndFirst = firstList[pFirst]
            
            if pSecond < 0: pSecond = 0
            iStartSecond, iEndSecond = secondList[pSecond]
            while iStartSecond <= iEndFirst:
                if iEndSecond < iStartFirst: 
                    pSecond += 1
                    if pSecond == nSecond: break
                    iStartSecond, iEndSecond = secondList[pSecond]
                    continue
                result.append([iStartSecond if iStartSecond >= iStartFirst else iStartFirst,
                              iEndSecond if iEndSecond <= iEndFirst else iEndFirst])
                pSecond += 1
                if pSecond == nSecond: break
                iStartSecond, iEndSecond = secondList[pSecond]
            pFirst += 1
            pSecond -= 1
        
        while pSecond < nSecond and secondList[pSecond][-1] > maxVal:
            pSecond += 1
        return result
        
result = Solution().intervalIntersection(
    [[0,5],[12,14],[15,18]],
    [[11,15],[18,19]]
)
print(result)