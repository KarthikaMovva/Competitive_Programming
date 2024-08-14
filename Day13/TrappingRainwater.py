class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        left, right = 0, len(height) - 1
        leftrange, rightrange = height[left], height[right]
        inTrap = 0

        while left < right:
            if leftrange < rightrange:
                left += 1
                leftrange = max(leftrange, height[left])
                inTrap += leftrange - height[left]
            else:
                right -= 1
                rightrange = max(rightrange, height[right])
                inTrap += rightrange - height[right]

        return inTrap
        