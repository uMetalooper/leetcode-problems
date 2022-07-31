from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        area = (different in positions) x (min of two heights)
        
        Using two pointers:
            - pFront: point at the front of list height and move forward
            -  pBack: point at the back  of list height and move backward

        While moving the pointers, calculate the area and compare with max 
            area recorded and overwrite it if it is smaller        

        Moving pointers strategy: move the smaller pointer in their direction, 
            because their are 3 possible cases:
                1. if the next height pointed by the pointer we just moved is 
                greater than 
            and if we move pFront or pBack, in either case, the different in 
            positions will decrease by one
        """
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