class Solution(object):
    def maxArea(self, height):
        left,right=0,len(height)-1
        record_max_area=0
        while left<right:
            breadth=right-left
            area=min(height[left],height[right])*breadth
            record_max_area=max(record_max_area,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return record_max_area