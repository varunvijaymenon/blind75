# python two sum

def two_sum(nums, target):


    # improved the efficieny by removing a loop
    for index, i in enumerate(nums):
        new_target = target - i

        if new_target in nums[index+1:]:
            return [index, nums.index(new_target, index+1)]
    return None
            



print(two_sum(nums = [2,7,11,15], target = 9))
print(two_sum(nums = [3,2,4], target = 6))
print(two_sum(nums = [3,3], target = 6))
