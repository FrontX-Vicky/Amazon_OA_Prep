def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = a + nums[left] + nums[right] 

            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                right -= 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1
        
    return res