# python two sum

def two_sum(nums, target):


    # Can be updated to check difference
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
            



print(two_sum(nums = [2,7,11,15], target = 9))
print(two_sum(nums = [3,2,4], target = 6))
print(two_sum(nums = [3,3], target = 6))
