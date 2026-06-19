# Problem 2: Container With Most Water
#
# You are given an integer array height of length n. There are n vertical lines drawn such that 
# the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
#
# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water the container can contain is 49 (lines at index 1 and 8).

def maxArea(height: list[int]) -> int:
    # TODO: Implement your solution here
    # Hint: Use a Two Pointer approach (left and right). 
    # Calculate the area, update the max area, and then move the pointer that points to the shorter line.
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area
        area = (right-left) * min(height[left], height[right])
        # Update the max area
        max_area = max(max_area, area)
        # Move the pointer that points to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area
