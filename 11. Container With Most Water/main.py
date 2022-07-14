from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        pFront = 0
        pBack = len(height)-1
        calcArea = lambda pf, pb: (pb-pf)*min(height[pb], height[pf])
        _maxArea = calcArea(pFront, pBack)
        while pFront != pBack:
            _area = calcArea(pFront, pBack)
            if _area > _maxArea: _maxArea = _area
            if height[pFront] < height[pBack]:
                pFront += 1
            else:
                pBack -= 1
        return _maxArea
        
result = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(result)